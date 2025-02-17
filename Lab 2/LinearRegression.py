# Linear Regression Model
import random

# Loss Function: Mean Squared Error
def compute_loss(X, y, w, b):
    m = len(y)
    predictions = [w * x + b for x in X]  # y = w * X + b
    loss = (1 / (2 * m)) * sum((pred - true) ** 2 for pred, true in zip(predictions, y))  # MSE loss function
    return loss

# Gradient Descent Function
def gradient_descent(X, y, w, b, learning_rate, iterations):
    m = len(y)
    losses = []
    
    for i in range(iterations):
        predictions = [w * x + b for x in X]  # y = w * X + b
        error = [pred - true for pred, true in zip(predictions, y)]
        
        dw = (1 / m) * sum(x * err for x, err in zip(X, error)) 
        db = (1 / m) * sum(error) 
        
        w -= learning_rate * dw
        b -= learning_rate * db
        
        loss = compute_loss(X, y, w, b)
        losses.append(loss)
        
        if i % 100 == 0:
            print(f"Iteration {i}, Loss: {loss:.4f}")
    
    return w, b, losses

# Sample data (X and y)
X = [i for i in range(1, 101)]  # Random data for X (1 to 100)
y = [4 + 3 * x + (random.uniform(-5, 5)) for x in X]  # y = 4 + 3 * X + noise

w = 0.0 
b = 0.0  
learning_rate = 0.0001
iterations = 1000
w, b, losses = gradient_descent(X, y, w, b, learning_rate, iterations)

# Print final learned parameters
print(f"Final learned weight: {w:.4f}")
print(f"Final learned bias: {b:.4f}")