class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        def derivative(x):
            return 2*x
        
        x_new = init
        for i in range(iterations):
            x_new = x_new - learning_rate * derivative(x_new)
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        return round(x_new, 5)