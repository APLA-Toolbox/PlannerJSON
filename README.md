## Solve the following problem

The FOX ROBOT is about to perform a mission. Help it find the right plan for the mission by finding the **least time** way to it's goal.

The FOX ROBOT can be any robot that has a set of possible states and a set of actions that the robot can do to change from one state to the other. Both the set of states and the set of actions are given as input in the form of json files.
Apart from the states and actions, a problem file is provided containing the initial and the desired state of the robot.
Some example input files can be found in the `input_files` folder.

The program should read the input files and output a json file containing the list of the actions our FOX ROBOT has to take in order to get from the initial to the goal state.
Two actions can be conscutive in the solution if the "state_end" of the first matches "state_start" of the second.
The first action in the output action list will have the "state_start" as the initial state from the
problem file (init) and the last action from the list will have at the "state_end" the goal state from
the problem file (goal) as they are described in the details below.

#### Structure of the input and output files:

Input:
* states.json  - a list of states that the robot can be in
* actions.json - a list of actions the robot can perform between states and the time it is required. The keys are:

```
action: name of the action
state_start: the inital state of the robot
state_end: the state of the robot after the action is performed
time: the amount of time taken by the robot to perform the action
```

* problem.json - the initial state of the robot and the final goal. The keys are"
```
init: initial state
goal: final state

Output 
* plan.json containing the fastest (least time) route to get from the initial state to the goal state, including the total time. The file could have the structure:
```json
{
    "actions": ["action1", "action2", "action3"],
    "time": 134
}
```

#### Aditional instructions

* Use programming language, libraries and db of your choice.
* Any kind of online and offline documentation and resources can be used.
* Fork this gitlab repository into a new one owned by you (private) and commit your solution in a development branch.
* We estimate that the problem should not take you longer than half a day.
* Even if you don't have a final solution it is important to commit your work.
For example even you don't find the optimal path (least time), we would like to
see a posible path as an output.
* Please leave comments in the code to help us understand your thought process.
