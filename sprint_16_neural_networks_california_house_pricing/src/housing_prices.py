import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras import Model
from keras.src.layers import Dense, Input, Dropout, BatchNormalization
from keras.src.models import Sequential
from keras.src.optimizers import Adam
from keras.src.regularizers import L2

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing

def load_data() -> pd.DataFrame:
    """
    Loads and returns the California housing dataset as a Pandas DataFrame.
    
    Returns:
    df (pd.DataFrame): California housing dataset.
    """
    housing = fetch_california_housing(as_frame=False)
    return pd.DataFrame(data=np.c_[housing['data'], housing['target']],
                        columns=housing['feature_names'] + ['MedHouseVal'])

def preprocess_data(df: pd.DataFrame) -> tuple[np.array, np.array, np.array, np.array, StandardScaler]:
    """
    Splits and preprocesses the data: handles missing values and scales numerical features.
    
    Parameters:
    df (pd.DataFrame): California housing dataset.

    Returns:
    X_train_scaled (np.ndarray): Scaled training features.
    X_test_scaled (np.ndarray): Scaled test features.
    y_train (np.ndarray): Training target variable.
    y_test (np.ndarray): Test target variable.
    scaler: StandardScaler object fit to training data.
    """
    # Handle missing values by fillinf with the median
    df.fillna(df.median(), inplace=True)

    # Drop target variable for feature selection
    X = df.drop(columns=['MedHouseVal'])
    y = df['MedHouseVal']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

def build_model(input_shape: int) -> Model:
    """
    Builds and returns a compiled neural network model.
    
    Parameters:
    input_shape (int): Number of features.

    Returns:
    model (Sequential): Compiled neural network model.
    """
    model = Sequential([
        # Input layer
        Input(shape=(input_shape,)),
        # Hidden layer 1
        Dense(64, activation='relu', kernel_regularizer=L2(0.01)),
        BatchNormalization(),
        Dropout(0.2),
        # Hidden layer 2
        Dense(32, activation='relu', kernel_regularizer=L2(0.01)),
        BatchNormalization(),
        Dropout(0.2),
        # Hidden layer 3
        Dense(16, activation='relu'),
        # Output layer
        Dense(1, activation='linear')
    ])

    adamOptimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=adamOptimizer, loss='mse', metrics=['mae'])
    return model

def train_model(model: Model,
                X_train: np.ndarray,
                y_train: np.ndarray,
                X_test: np.ndarray,
                y_test: np.ndarray, epochs=50, batch_size=32):
    """
    Trains the model and returns the training history.
    
    Parameters:
    model (Sequential): Compiled neural network model.
    X_train (np.ndarray): Scaled training features.
    y_train (np.ndarray): Training target variable.
    X_test (np.ndarray): Scaled test features.
    y_test (np.ndarray): Test target variable.
    epochs (int): Number of training epochs.
    batch_size (int): Batch size for training.

    Returns:
    history: Training history.
    """
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test),
                        epochs=epochs, batch_size=batch_size, verbose=2)
    return history

def evaluate_model(model: Model, X_test: np.ndarray, y_test: np.ndarray) -> tuple[float, float]:
    """
    Evaluates the model and returns the test loss and MAE.

    Parameters:
    model (Sequential): Trained neural network model.
    X_test (np.ndarray): Scaled test features.
    y_test (np.ndarray): Test target variable.

    Returns:
    loss (float): Test loss.
    mae (float): Test mean absolute error.
    """
    loss, mae = model.evaluate(X_test, y_test, verbose=2)
    return loss, mae

def plot_loss(history: any) -> None:
    """Plots the training and validation loss curves."""
    plt.figure(figsize=(12, 5))
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('MSE Loss')
    plt.legend()
    plt.title('Model Training Loss Curve')
    plt.show()

def plot_predictions(y_test: np.ndarray, y_pred: np.ndarray) -> None:
    """Plots actual vs predicted prices."""
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='b')
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.title('Actual vs Predicted House Prices')
    plt.show()

def predict_house_price(model: Model, house_features: list[float], scaler: StandardScaler) -> float:
    """
    Predicts the price of a single house.
    
    Parameters:
    model (Sequential): Trained neural network model.
    house_features (list): List of house features (same order as training data).
    scaler: Scaler object used for data preprocessing.
   
    Returns:
    predicted_price (float): Predicted house price.
    """
    # Convert input to a NumPy array and reshape for model
    house_features_array = pd.DataFrame(data=[house_features],
                                        columns=fetch_california_housing(as_frame=True)['feature_names'])

    # Scale the input features using the same scaler used in training
    house_features_scaled = scaler.transform(house_features_array)

    # Predict price
    predicted_price = model.predict(house_features_scaled)
    return predicted_price.item()

# Main execution
if __name__ == "__main__":
    # Step 1: Load data
    df = load_data()

    # Step 2: Preprocess data
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

    # Step 3: Build and train the model
    model = build_model(X_train.shape[1])
    history = train_model(model, X_train, y_train, X_test, y_test)

    # Step 4: Evaluate the model
    loss, mae = evaluate_model(model, X_test, y_test)
    print(f"Test Mean Absolute Error: {mae:.2f}")

    # Step 5: Plot loss and predictions
    plot_loss(history)
    y_pred = model.predict(X_test)
    plot_predictions(y_test, y_pred)

    # Example new house features (same order as dataset)
    new_house = [8.32, 41.0, 6.984127, 1.02381, 322.0, 2.555556, 37.88, -122.23]  # Example house data

    # Step 6: Predict the house price
    predicted_price = predict_house_price(model, new_house, scaler)
    print(f"Predicted House Price: ${predicted_price * 100000:.2f}")  # Scale back to a realistic price
