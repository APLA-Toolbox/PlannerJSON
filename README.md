## Solve the following problem

The FOX ROBOT is about to perform a mission. Help it find the right plan for the mission by finding the **least time** way to it's goal.

The FOX ROBOT can be any robot that has a set of possible states and a set of actions that the robot can do to change from one state to the other. Both the set of states and the set of actions are given as input in the form of json files.
Apart from the states and actions, a problem file is provided containing the initial and the desired state of the robot.
Some example input files can be found in the `input_files` folder.

The program should read the input files and output a json file containing the list of the actions our FOX ROBOT has to take in order to get from the initial to the goal state.

#### Structure of the input and output files:

Input:
states.json  - a list of states that the robot can be in
actions.json - a list of actions the robot can perform between states and the time it is required:
problem.json - the initial state of the robot and the final goal

Output - a json file plan.json containing the fastest (least time) route to get from the initial state to the goal state, including the total time.

#### Aditional instructions

* Use programming language, libraries and db of your choice.
* Any kind of online and offline documentation and resources can be used.
* Commit your work to this gitlab repository, in a development branch.
* We estimate that the problem should not take you longer than half a day.
Even if you don't have a final solution it is important to commit your work.
* Please leave comments in the code to help us understand your thought process.
