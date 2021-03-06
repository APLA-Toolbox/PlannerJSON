from utils import *
from Graph import Graph
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSON Files")
    parser.add_argument("--path-to-pb", type=str, help="Path to the Problem Folder",
                        required=True)
    args = parser.parse_args()
    
    action_filename = "actions.json" if args.path_to_pb[-1] == "/" else "/actions.json"
    try:
        actions = get_actions_from_json(args.path_to_pb+action_filename)
    except Exception as e:
        print(f"Failed to parse actions file: %s" % (str(e),))
        exit(-1)

    problem_filename = "problem.json" if args.path_to_pb[-1] == "/" else "/problem.json"
    try:
        problem = get_problem_from_json(args.path_to_pb+problem_filename)
    except Exception as e:
        print("Failed to parse problem file: " + str(e))
        exit(-1)

    state_filename = "states.json" if args.path_to_pb[-1] == "/" else "/states.json"
    try:
        states = get_states_from_json(args.path_to_pb+state_filename)
    except Exception as e:
        print("Failed to parse states file: " + str(e))
        exit(-1)

    try:
        graph = Graph(states, actions)
        states, actions, metrics = graph.astar_search(problem, graph.zero_heuristic)
    except Exception as e:
        print("Failed to solve the problem: " + str(e))
        exit(-1)

    try:
        plan_filename = "plan.json" if args.path_to_pb[-1] == "/" else "/plan.json"
        generate_output_solved(args.path_to_pb+plan_filename, 
                               actions,
                               states,
                               metrics)
    except Exception as e:
        print("Failed to populate plan file: " + str(e))
    