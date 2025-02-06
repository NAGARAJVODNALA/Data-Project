import numpy as np
import random
import time
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# -1 is origin, 0 is road, 1 is wall, 2 is goal 
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

def init_q_table(maze):
    Q = np.zeros(maze.shape).tolist()
    for i, row in enumerate(Q):
        for j, _ in enumerate(row):
            Q[i][j] = [0, 0, 0, 0]  # up, down, left, right
    return np.array(Q, dtype='f')

def get_action(Q_table, state, action_list, e_greedy=0.8):
    if random.random() > e_greedy:
        return random.choice(action_list)
    else:
        Qsa = Q_table[state].tolist()
        return action_list[Qsa.index(max(Qsa))]

def get_next_max_q(Q_table, state):
    return max(np.array(Q_table[state]))

def update_q_table(Q_table, state, action, next_state, reward, lr=0.7, gamma=0.9):
    Qs = Q_table[state]
    Qsa = Qs[action]
    Qs[action] = (1 - lr) * Qsa + lr * (reward + gamma * get_next_max_q(Q_table, next_state))
    return Q_table

def get_next_state(state, action):
    row, column = state
    if action == 'up':
        row -= 1
    elif action == 'down':
        row += 1
    elif action == 'left':
        column -= 1
    elif action == 'right':
        column += 1
    nextState = (row, column)
    
    try:
        # Boundary or wall check
        if row < 0 or column < 0 or maze[row, column] == 1:
            return [state, False]
        # Goal reached
        elif maze[row, column] == 2:
            return [nextState, True]
        # Move forward
        else:
            return [nextState, False]
    except IndexError:
        return [state, False]

def do_action(state, action):
    nextState, result = get_next_state(state, action)
    if nextState == state:
        reward = -10
    elif result:
        reward = 100
    else:
        reward = -1
    return [reward, nextState, result]

def visualize_maze(maze, agent_position):
    plt.clf()
    cmap = mcolors.ListedColormap(['blue', 'white', 'black', 'green'])
    norm = mcolors.BoundaryNorm([-1, 0, 1, 2, 3], cmap.N)

    maze_copy = maze.copy()
    r, c = agent_position
    maze_copy[r, c] = 3  # Mark agent's position with a different color

    plt.imshow(maze_copy, cmap=cmap, norm=norm)
    plt.xticks([]), plt.yticks([])  # Hide grid ticks
    plt.draw()
    plt.pause(0.1)

# Initialize Q-table and agent's starting position
initState = (np.where(maze == -1)[0][0], np.where(maze == -1)[1][0])
Q_table = init_q_table(maze)
action_list = ['up', 'down', 'left', 'right']

y = []
plt.figure(figsize=(5, 5))

for j in range(0, 30):
    state = initState
    i = 0

    while True:
        i += 1
        visualize_maze(maze, state)  # Show agent's position
        action = get_action(Q_table, state, action_list, 0.9)
        reward, next_state, result = do_action(state, action)
        Q_table = update_q_table(Q_table, state, action_list.index(action), next_state, reward)
        state = next_state
        
        if result:  # If goal is reached, stop training
            y.append(i)
            print(f"Goal reached in {i} steps on iteration {j+1}!")
            break

plt.show()  # Final display after all iterations

# Plot learning curve
plt.plot(np.arange(len(y)), y)
plt.xlabel('Iteration')
plt.ylabel('Steps to Goal')
plt.title('Q-Learning Progress')
plt.show()
