[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AFaM_unx)
# Sprint 13. Supervised Learning - Regression

### Task 1. Linear Regression with CSV Data and Model Evaluation

#### **Problem Description**

You are tasked with creating a Python script that:
1. Implements **Linear Regression** to predict a target variable from features in a CSV file.
2. Evaluates the model using **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, **Root Mean Squared Error (RMSE)**.
3. Reads data from a CSV file, ensuring the file isn't empty.
4. Visualizes the relationship between the feature and target variable using **Matplotlib**.
5. Includes **unit tests** to:
   - Validate the presence of the CSV reading function.
   - Verify that the data read from the CSV is not empty.
   - Test the output of Linear Regression.

The code will be divided into two parts:
- A Python script in the `src` folder implementing the solution.
- A Python script in the `test` folder containing `pytest` tests.

---

### Folder Structure
```
project/
│
├── src/
│   ├── linear_regression.py
│
├── test/
│   ├── test_linear_regression.py
│
├── data.csv  # Example dataset
```

---

### Example CSV File (`data.csv`)
```csv
Feature,Target
1,2
2,4
3,6
4,8
5,10
```


---

### Explanation of the Code

#### **`src/linear_regression.py`**
1. **`read_csv(file_path)`**:
   - Reads a CSV file using `pandas`.
   - Ensures the file isn't empty, raising a `ValueError` if it is.

2. **`visualize_data(data, x_column, y_column)`**:
   - Visualizes the scatter plot of the data using **Matplotlib**.

3. **`linear_regression_with_metrics(data, x_column, y_column)`**:
   - Trains a Linear Regression model using `scikit-learn`.
   - Evaluates the model using metrics: MAE, MSE, RMSE.
   - Visualizes the regression line over the test data.

#### **`test/test_linear_regression.py`**
1. **`test_read_csv_function_exists()`**:
   - Verifies the presence of the `read_csv` function.

2. **`test_csv_not_empty()`**:
   - Creates a non-empty temporary CSV file and checks if the data is correctly read.

3. **`test_empty_csv()`**:
   - Creates an empty temporary CSV file and ensures the `read_csv` function raises a `ValueError`.

4. **`test_linear_regression_output()`**:
   - Creates a valid dataset and tests that the Linear Regression function runs without errors.


## Task 2. Polynomial Regression for Predicting House Prices

#### **Problem Description**
You are tasked with implementing **Polynomial Regression** to predict house prices based on house sizes. Your solution should:  
1. Read a dataset (`house_data.csv`) containing house sizes and prices.  
2. Train a **Polynomial Regression** model to capture non-linear relationships between house size and price.  
3. Evaluate the model using metrics:  
   - **Mean Absolute Error (MAE)**  
   - **Mean Squared Error (MSE)**  
   - **Root Mean Squared Error (RMSE)**  
4. Visualize the results using **Matplotlib**, plotting the original data points and the regression curve.  
5. Write unit tests using `pytest` to validate the implementation.

---

### **Example Input Dataset**: `house_data.csv`
```csv
Size,Price
1000,150000
1200,170000
1500,200000
1800,250000
2000,300000
```
---

