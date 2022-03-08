from time import time
from Problem import Problem
from State import State
from Action import Action
import json
from typing import Dict
from Metrics import Metrics


'''
Populates a dictionary with a JSON file
'''
def populate(json_file: str) -> Dict:
    json_dict = dict()
    with open(json_file, 'r') as j:
        json_dict = json.loads(j.read())
    return json_dict

'''
Populates a dictionary of Action objects from a JSON file
'''
def get_actions_from_json(json_file_actions):
    actions = dict()
    parsed_actions = populate(json_file_actions)
    for action in parsed_actions["actions"]:
        in_state = State(action["state_start"])
        out_state = State(action["state_end"])
        actions[action["action"]] = Action(
                name=action["action"],
                state_start=in_state,
                state_end=out_state,
                time=action["time"],
            )
    return actions
    

'''
Populates a dictionary of State objects from a JSON file
'''
def get_states_from_json(json_file_states):
    parsed_states = populate(json_file_states)
    states = dict()
    for state in parsed_states["states"]:
        states[state] = State(state)
    return states


'''
Populate a Problem object from a JSON file
'''
def get_problem_from_json(json_file_problem):
    parsed_problem = populate(json_file_problem)
    problem = Problem(State(parsed_problem["init"]), State(parsed_problem["goal"]))
    return problem


'''
Dump the computed Plan with different informations in a Plan JSON file
'''
def generate_output_solved(json_file_plan, actions_path, states_path, metrics: Metrics):
    data = {
        "actions": [],
        "states_sequence": [],
    }
    for action in actions_path:
        data["actions"].append(action.name)
    
    for state in states_path:
        data["states_sequence"].append(state.name)

    data["cost"] = metrics.total_cost
    data["deadend_states"] = metrics.deadend_states
    data["heuristic_runtimes"] = metrics.heuristic_runtimes
    data["evaluated_nodes"] = metrics.n_evaluated
    data["generated_nodes"] = metrics.n_generated
    data["opened_nodes"] = metrics.n_opened
    data["reopened_nodes"] = metrics.n_reopened
    data["runtime"] = metrics.runtime
    data["expanded_nodes"] = metrics.n_expended

    with open(json_file_plan, 'w') as outfile:
        json.dump(data, outfile, indent=2)


'''
Stringify a list of objects
'''
def stringify_list_objects(list_of_objects):
    return ''.join(str(item) for item in list_of_objects)