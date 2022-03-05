from time import time
from Problem import *
from State import *
from Action import *
import json

def populate(json_file):
    json_dict = dict()
    with open(json_file, 'r') as j:
        json_dict = json.loads(j.read())
    return json_dict


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
    

def get_states_from_json(json_file_states):
    parsed_states = populate(json_file_states)
    states = dict()
    for state in parsed_states["states"]:
        states[state] = State(state)
    return states


def get_problem_from_json(json_file_problem):
    parsed_problem = populate(json_file_problem)
    problem = Problem(State(parsed_problem["init"]), State(parsed_problem["goal"]))
    return problem

def generate_output_solved(json_file_plan, actions_path, states_path, total_time):
    data = {
        "actions": [],
        "states_sequence": [],
    }
    for action in actions_path:
        data["actions"].append(action.name)
    
    for state in states_path:
        data["states_sequence"].append(state.name)

    data["time"] = total_time

    with open(json_file_plan, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def stringify_list_objects(list_of_objects):
    return ''.join(str(item) for item in list_of_objects)