import keras
import numpy as np
import matplotlib.pyplot as plt
from keras import Sequential, Model
from keras.src.layers import Dense, Input
from keras.src.optimizers import Adam

def true_function(x):
    return np.sin(x) + 0.1 * x ** 2

def generate_training_data(seed=42, num_samples=500) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate random training data.
    
    Parameters:
    seed (int): Random seed for reproducibility.
    num_samples (int): Number of training samples.

    Returns:
    x_train (np.ndarray): Input training data.
    y_train (np.ndarray): Output training data.
    """
    np.random.seed(seed)
    x_train = np.random.uniform(-10, 20, num_samples).reshape(-1, 1)
    y_train = true_function(x_train) + np.random.normal(0, 0.1, size=x_train.shape)
    return x_train, y_train

def build_model() -> Sequential:
    """
    Builds and returns a neural network model.
    
    Returns:
    model (keras.Model): Neural network model.
    """
    model = keras.Sequential([
        Input(shape=(1,)),
        Dense(64, activation='relu'),
        Dense(64, activation='relu'),
        Dense(1, activation='linear')
    ])
    adamOptimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=adamOptimizer, loss='mse', metrics=['mae'])
    return model

def train_model(model: Model, x_train: np.ndarray, y_train: np.ndarray, epochs=100, batch_size=32) -> any:
    """
    Trains the model on the training data.
    
    Parameters:
    model (keras.Model): Neural network model.
    x_train (np.ndarray): Input training data.
    y_train (np.ndarray): Output training data.
    epochs (int): Number of training epochs.
    batch_size (int): Batch size for training.

    Returns:
    history: Training history.
    """
    history = model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, verbose=2)
    return history

def evaluate_model(model: Model, x_test: np.ndarray) -> np.ndarray:
    """
    Evaluates the model on the test data
    
    Parameters:
    model (keras.Model): Trained neural network model.
    x_test (np.ndarray): Input test data.

    Returns:
    y_pred (np.ndarray): Predicted output
    """
    y_pred = model.predict(x_test)
    return y_pred

def visualize_results(x_train, y_train, x_test, y_pred):
    """Visualize the training data and model predictions."""
    plt.figure(figsize=(8, 5))
    plt.scatter(x_train, y_train, label="Training Data", alpha=0.3)
    plt.plot(x_test, true_function(x_test), label="True Function", color="green", linestyle="dashed")
    plt.plot(x_test, y_pred, label="NN Prediction", color="red")
    plt.legend()
    plt.title("Function Approximation using Neural Network")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

def predict(model: Model, x_new: int) -> float:
    """
    Predicts the value of a new point.
    
    Parameters:
    model (keras.Model): Trained neural network model.
    x_new (float): New input value.

    Returns:
    predicted_value (float): Predicted output value.
    """
    x_new_ = np.array([[x_new]])
    predicted_value = model.predict(x_new_)
    return predicted_value.item()

# Main Execution
if __name__ == "__main__":
    # Step 1: Generate Data
    x_train, y_train = generate_training_data()
    x_test = np.linspace(-10, 10, 100).reshape(-1, 1)
    
    # Step 2: Build and Train Model
    model = build_model()
    train_model(model, x_train, y_train)
    
    # Step 3: Evaluate Model
    y_pred = evaluate_model(model, x_test)
    
    # Step 4: Visualize Results
    visualize_results(x_train, y_train, x_test, y_pred)
    
    # Step 5: Predict a new value
    x_new = 7
    y_new_pred = predict(model, x_new)
    print(f"Predicted value at x={x_new}: {y_new_pred:.4f}")
