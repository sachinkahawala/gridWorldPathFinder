# gridWorldPathFinder
 Optimal path finding in a 2D grid with reinforcement learning.
 Policy iteration with Dynamic programming is used to improve the policy.
Finding the optimal pollicy for a agent that has 4 possible actions including up, down, left and right.

![image](https://user-images.githubusercontent.com/25722196/70846513-0367c180-1e80-11ea-81d6-abbb0514e966.png)

The grid may contain obstacles where the agent won’t be able to penetrate through. Which will be marked in green in the GUI. Hitting in to a obstacle is given a reward of -1000 and for each step the agent take is given a reward of -1. Agents goal is to maximize the reward.
Implementation assumes that each action is deterministic, that is, the agent will go where it intends to go. For instance, when the agent decides to take action up at (2, 0), it will land in (1, 0). The tragets are the ultimate goals of the agent, it will try to arrive at the nearest target with minimum steps as possible. The targets are shown in blue in the GUI. 

![image](https://user-images.githubusercontent.com/25722196/70846598-cb14b300-1e80-11ea-98df-7435e278aa90.png)

If no targets are reachable it will try to arrive at the closest arrivalbe cell in the grid. For each cell best policy (which actionss to take in order to arive at the closest target) will be shown after calculating the optimal path. 

![image](https://user-images.githubusercontent.com/25722196/70846629-2ba3f000-1e81-11ea-8b14-9286f3a2f8c7.png)

A multi target instance is shown below.

![image](https://user-images.githubusercontent.com/25722196/70846759-7eca7280-1e82-11ea-8276-f6650c89cbb5.png)

A larger grid example is shown below. 

![image](https://user-images.githubusercontent.com/25722196/70846736-38751380-1e82-11ea-9ca8-8cad37c0ba1b.png)



