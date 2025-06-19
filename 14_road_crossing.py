# Assignment One train RL agent to navigate to cross the road with action right, left, right

# Import necessary libraries
import numpy as np
import random
import time

# Define environment parameters
num_states = 4  # States: 0=start, 1=right, 2=right->left, 3=success
actions = 2  # 0: Look Right, 1: Look Left

# Initialize Q-table
Q = np.zeros((num_states, actions))

# Define parameters
episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.2  # Probability of taking a random action (exploration)

# Training loop
for episode in range(episodes):
    state = 0  # Start at beginning of sequence
    step_count = 0

    while state != 3:  # Until goal reached
        # Action selection (Epsilon-greedy policy)
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit best action

        # Take action based on environment logic
        if state == 0 and action == 0:
            next_state = 1
            reward = 0
        elif state == 1 and action == 1:
            next_state = 2
            reward = 0
        elif state == 2 and action == 0:
            next_state = 3
            reward = 10
        else:
            next_state = 0
            reward = -5  # Reset for wrong sequence

        # Q-learning update
        Q[state, action] += learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        # Transition to next state
        state = next_state
        step_count += 1
        time.sleep(0.05)
        print(f"Episode {episode+1}, state: {state}, Q: {Q[state]}")

print(f"Episode {episode+1} finished in {step_count} steps.")


# Show Learned Q-table
print("Q-table:")
print(Q)

# Test the trained agent
state = 0
steps = 0
action_names = {0: "RIGHT", 1: "LEFT"}

print("\nAgent path to goal:")

while state != 3:
    action = np.argmax(Q[state])  # Pick best learned action

    # Environment logic
    if state == 0 and action == 0:
        next_state = 1
    elif state == 1 and action == 1:
        next_state = 2
    elif state == 2 and action == 0:
        next_state = 3
    else:
        next_state = 0  # Reset

    print(
        f"Step {steps}: State {state} -> Action {action_names[action]} -> Next State {next_state}"
    )
    state = next_state
    steps += 1
   
print(f"\nCorrectly completed sequence in {steps} steps.")
print("\nFinal Q-table:")
print(Q)
