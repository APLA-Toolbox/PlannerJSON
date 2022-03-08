from collections import deque
from TransitionMatrix import TransitionMatrix
from State import State
from Problem import Problem
from Action import Action
from typing import Dict, List, Tuple
from Node import Node
from Heuristics import GoalCountHeuristic, ZeroHeuristic
from time import time as now
from Metrics import Metrics

class Graph:
    def __init__ (self, states: Dict, actions: Dict):
        self.states = states
        self.transition_matrix = TransitionMatrix(actions, states)
        
        self.zero_heuristic = ZeroHeuristic(states)
        self.goal_count_heuristic = GoalCountHeuristic()
        
        
        # Could Do: generic heuristics
        # Could Do: DFS Search
        # Could Do: BFS Search
        # Could Do: A* (based on found heuristics)
        # Could Do: Greedy Best First Search (based on found heuristics)
    
    def __get_successors(self, node: Node) -> List[Tuple[Action, State, int]]:
        return self.transition_matrix[node.state.name]

    def astar_search(self, problem: Problem, heuristic) -> Tuple[List[State], List[Action], Metrics]:
        # Initialization of the Problem
        # Instantiate Nodes using State and Cost
        # Open and Close list are represented using flags in the Node object
        time_start = now()
        metrics = Metrics()
        heuristic.set_goal_state(problem.goal_state)
        start_node = Node(problem.init_state, 0, False, True, heuristic, None)
        nodes = dict()
        nodes[problem.init_state.name] = start_node
        self.reached = False

        # As long as we have nodes in the open list (or here set as is_open, we keep expanding)
        while self.__count_open_nodes(nodes) > 0:
            # Nodes are sorted using the __lt__ overload
            # This snippet gets the minimum f_cost among all open nodes in the dict
            current_key = min([n for n in nodes if nodes[n].is_open], key=(lambda k: nodes[k].f_cost))
            current_node = nodes[current_key]

            metrics.n_evaluated += 1

            # If we have reached the goal state, we exit
            if current_node.state == problem.goal_state:
                print("Found minimal set of actions.")
                states_path = self.__retrace_states(current_node)
                actions_path = self.__retrace_actions(current_node)
                metrics.total_cost = current_node.g_cost
                metrics.runtime = now() - time_start
                return states_path, actions_path, metrics

            # Mark the current node as closed
            current_node.is_closed = True
            current_node.is_open = False

            # if nodes opened > bound: break -> not found

            successors = self.__get_successors(current_node)
            
            if not successors:
                metrics.deadend_states += 1

            for action, child_state, time in successors:
                metrics.n_expended += 1

                # If we already generated the node
                if child_state.name in nodes:
                    if nodes[child_state.name].is_closed:
                        # If the node is in the closed list,
                        # We don't do anything with this successor
                        continue
                    
                    if not nodes[child_state.name].is_open:
                        # If the child is not in the open list
                        nodes[child_state.name] = Node(
                            child_state,
                            current_node.g_cost + time,
                            False,
                            True,
                            heuristic,
                            action,
                            current_node
                        )
                        metrics.n_opened += 1
                    
                    else:
                        # If we've already opened it, let's check if this is a better path
                        if current_node.g_cost + time < nodes[child_state.name].g_cost:
                            nodes[child_state.name] = Node(
                                child_state,
                                current_node.g_cost + time,
                                False,
                                True,
                                heuristic,
                                action,
                                current_node
                            )
                        metrics.n_reopened += 1
                else:
                    # If it hasn't been generated, generate it
                    nodes[child_state.name] = Node(
                                child_state,
                                current_node.g_cost + time,
                                False,
                                True,
                                heuristic,
                                action,
                                current_node   
                    )
                    metrics.n_generated += 1        
        
        # If we expanded all nodes without finding the goal state, the path wasn't found
        print("Path not found!")
        metrics.runtime = now() - time_start
        return [problem.init_state], [], metrics

    def __count_open_nodes(self, nodes) -> int:
        i = 0
        for _, node in nodes.items():
            if node.is_open:
                i += 1
                break
        return i

    def __retrace_states(self, last_node) -> List[State]:
        """
        Retrace the path from parents to parents until start node
        """
        current_node = last_node
        path = []
        while current_node is not None:
            path.append(current_node.state)
            current_node = current_node.parent
        path.reverse()
        return path
    
    def __retrace_actions(self, last_node) -> List[Action]:
        """
        Retrace the path from parents to parents until start node
        """
        current_node = last_node
        path = []
        while current_node is not None:
            path.append(current_node.action)
            current_node = current_node.parent
        path.reverse()
        return path[1:]