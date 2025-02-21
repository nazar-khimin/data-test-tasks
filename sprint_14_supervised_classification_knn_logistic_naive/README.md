[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hnALotgJ)
# MLDS_sprint14-SL-Classification

## Task 1. Binary Classification Using Logistic Regression

#### **Problem Description**
You are tasked with implementing **Logistic Regression** for a binary classification problem. Your solution should:
1. Read a dataset (`data.csv`) containing two features (`Feature1` and `Feature2`) and a target (`Target` with values 0 or 1).  
2. Train a **Logistic Regression** model to classify the target variable based on the two features.
3. Evaluate the model using metrics:
   - **Accuracy**
   - **Precision**
   - **Recall**
   - **F1-Score**
4. Visualize the data and the decision boundary using **Matplotlib**.
5. Write unit tests using `pytest` to validate the implementation, including checking for file reading and logistic regression output.
6. Include a function to generate a synthetic dataset and save it to a CSV file.


### Expected Output

- **Script Output**:
  - Evaluation metrics: Accuracy, Precision, Recall, F1-Score.
  - Visualization of the decision boundary.


## Task 2. Classifying Data Using Decision Trees

### Task: Classifying Data Using Decision Trees

#### **Problem Description**
You are tasked with building a **Decision Tree Classifier** to classify data into two categories. Your solution should:
1. Generate a synthetic dataset (`data.csv`) with two features and a binary target variable.
2. Train a **Decision Tree Classifier** on the dataset.
3. Evaluate the classifier using metrics:
   - **Accuracy**
   - **Precision**
   - **Recall**
   - **F1-Score**
4. Visualize the decision boundaries of the Decision Tree model using **Matplotlib**.
5. Write unit tests using `pytest` to validate the implementation, including file reading and classification logic.


### Expected Output

- **Script Output**: Evaluation metrics and a decision boundary visualization.


## Task 3. Classifying Data Using K-Nearest Neighbors (K-NN)

#### **Problem Description**
You are tasked with implementing a **K-Nearest Neighbors (K-NN)** classifier to predict binary class labels based on two features. Your solution should:
1. Generate a synthetic dataset (`data.csv`) with two features and a binary target variable.
2. Train a **K-NN Classifier** on the dataset.
3. Evaluate the classifier using metrics:
   - **Accuracy**
   - **Precision**
   - **Recall**
   - **F1-Score**
4. Visualize the decision boundaries using **Matplotlib**.
5. Write unit tests using `pytest` to validate the implementation, including file reading, data generation, and model evaluation.


### Expected Output

- **Script Output**:
  - Evaluation metrics: Accuracy, Precision, Recall, F1-Score.
  - Visualization of the decision boundary.

## Task 4. Binary Classification Using Naive Bayes

#### **Problem Description**
You are tasked with implementing a **Naive Bayes Classifier** for a binary classification problem. Your solution should:
1. Generate a synthetic dataset (`data.csv`) with two features and a binary target variable.
2. Train a **Naive Bayes Classifier** using the dataset.
3. Evaluate the classifier using metrics:
   - **Accuracy**
   - **Precision**
   - **Recall**
   - **F1-Score**
4. Visualize the decision boundaries of the classifier using **Matplotlib**.
5. Write unit tests using `pytest` to validate the implementation, including file reading, data generation, and model evaluation.


### Expected Output

- **Script Output**:
  - Evaluation metrics: Accuracy, Precision, Recall, F1-Score.
  - Visualization of the decision boundary.



## Running Tests

This project uses [pytest](https://pytest.org) for testing. Follow these steps to run the tests:

1. **Install dependencies**:  
   Ensure all required dependencies are installed. If a `requirements.txt` file is provided, run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run all tests**:
   To execute all tests in the project, use the following command:
   ```bash
   pytest
   ```
3. **Enable detailed logging**:
   To enable detailed logging during the test run, use:
   ```bash
   pytest -o log_cli=true --log-cli-level=INFO

   ```
