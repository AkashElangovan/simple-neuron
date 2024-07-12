import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def restaurant_decision_nn(inputs):
    weights = np.array([0.9, 0.7, 0.6, 0.8, 0.4])
    normalized_inputs = np.array(inputs)
    normalized_inputs[0] = (inputs[0] - 1) / 4  # Budget: 1-5 to 0-1
    normalized_inputs[1] = 1 - inputs[1]  # Food at Home: 0-1 to 1-0 (reverse)
    normalized_inputs[2] = (inputs[2] - 1) / 4  # Time: 1-5 to 0-1
    normalized_inputs[3] = (inputs[3] - 1) / 4  # Health: 1-5 to 0-1
    normalized_inputs[4] = (inputs[4] - 1) / 4  # Weather: 1-5 to 0-1
    weighted_sum = np.dot(normalized_inputs, weights)
    output = sigmoid(weighted_sum)
    threshold = 0.5
    return "Yes" if output > threshold else "No"
print("Please provide the following information:")
budget = float(input("1. Budget (1 = no money, 5 = enough money): "))
food_at_home = int(input("2. Food at Home (0 = no, 1 = yes): "))
time = float(input("3. Time (1 = no time, 5 = enough time): "))
health = float(input("4. Health Considerations (1 = not healthy, 5 = healthy): "))
weather = float(input("5. Weather (1 = bad, 5 = good): "))
if not (1 <= budget <= 5 and food_at_home in [0, 1] and 1 <= time <= 5 and 1 <= health <= 5 and 1 <= weather <= 5):
    print("Invalid input. Please ensure you're using the correct ranges for each factor.")
else:
    inputs = [budget, food_at_home, time, health, weather]
    decision = restaurant_decision_nn(inputs)
    print(f"\nBased on your inputs, the neural network suggests: {decision}, you should {'go' if decision == 'Yes' else 'not go'} to a restaurant for dinner today.")