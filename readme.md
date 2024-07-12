# Restaurant Decision Neural Model

## Overview
This project implements a simple neural model to help decide whether to go to a restaurant for dinner. It's designed as an educational tool to demonstrate fundamental concepts of neural networks and decision-making algorithms.

## Key Features
- Built entirely from scratch using only NumPy
- No complex machine learning libraries required
- Perfect for beginners learning about neural networks
- Demonstrates core concepts like weights, activation functions, and decision boundaries

## How It Works
The model uses a single artificial neuron (similar to a perceptron) to make a decision based on 5 inputs:

1. Budget (1-5 scale)
2. Food at Home (Binary: 0 or 1)
3. Time Available (1-5 scale)
4. Health Considerations (1-5 scale)
5. Weather (1-5 scale)

These inputs are weighted and passed through a sigmoid activation function to produce a yes/no decision.

## Educational Value
- Understand how neural networks make decisions without the complexity of full-scale libraries
- See the direct impact of weights on the decision-making process
- Learn about activation functions and their role in neural computations
- Great starting point before diving into more complex neural network architectures

## Model Visualization
![Single Neuron Model Diagram](single_neuron_model_diagram.svg)

## Requirements
- Python 3.x
- NumPy (only used for basic array operations)

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/restaurant-decision-model.git
   ```
2. Install NumPy (if not already installed):
   ```
   pip install numpy
   ```

## Usage
Run the script and follow the prompts to input your ratings for each factor:

```python
python restaurant_decision.py
```

## Code Structure
- `restaurant_decision.py`: Contains the main neural model and user interface. The code is thoroughly commented to explain each step of the process.

## Learning Opportunities
- Modify the weights to see how they affect the decision
- Experiment with different activation functions
- Add more input factors to the decision-making process
- Implement a simple learning algorithm to adjust weights based on feedback

## Limitations
- This is a simplified model, not a full neural network
- Weights are pre-defined, not learned from data
- Can only capture linear relationships between inputs and the decision

## Future Improvements for Learning
- Add a simple backpropagation algorithm to demonstrate learning
- Implement multiple layers to show how deep neural networks work
- Create visualizations of decision boundaries as weights change

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/restaurant-decision-model/issues) if you want to contribute or have ideas for making this educational tool even better.

## License
This project is open source and available under the [MIT License](LICENSE.md).