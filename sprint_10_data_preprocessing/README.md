# Sprint 10. Data Preprocessing

## **Task 1: Removing Duplicates and Handling Missing Values**
You are provided with a dataset that contains both duplicate rows and missing values. Your task is twofold:

1. **Remove Duplicate Rows**: First, identify and remove any duplicate rows in the dataset to ensure data integrity.
  
2. **Handle Missing Values**: After removing duplicates, handle the missing values by dropping rows that have more than 50% of their columns with missing data. This is critical for ensuring that the dataset remains useful for further analysis without being skewed by too much incomplete information.


## **Task 2: Simple Imputation of Missing Values**
You are provided with a dataset that contains missing values across multiple columns. Your task is to impute these missing values using different imputation techniques for each column:

1. **Column A**: Impute missing values using the mean of the non-missing values in this column.
2. **Column B**: Impute missing values using the median of the non-missing values in this column.
3. **Column C**: Impute missing values using the mode (most frequent value) of the non-missing values in this column.

## **Task 3: Data Scaling and Normalization**
You are provided with a dataset that contains numerical features with varying ranges and distributions. Your task is to apply three different scaling and normalization techniques to prepare the data for machine learning algorithms:

1. **Min-Max Scaling**: Rescale the data to a fixed range between 0 and 1. This technique is useful when the data needs to be normalized to a specific range, often as a preprocessing step for algorithms that rely on distances (e.g., K-Nearest Neighbors).
  
2. **Z-Score Normalization (Standardization)**: Adjust the data so that each feature has a mean of 0 and a standard deviation of 1. This technique is essential for algorithms that assume data follows a standard normal distribution or are sensitive to different scales (e.g., linear regression).

3. **Robust Scaling**: Scale the data based on the median and interquartile range (IQR), making it less sensitive to outliers. This method is particularly useful when dealing with data that contains outliers, as it reduces their impact on the scaling process.

## **Task 4: Advanced BMI Calculation with Categorization**
You are provided with a dataset containing the `height` and `weight` of several individuals. Your task is to calculate the Body Mass Index (BMI) for each individual and then categorize them into `Underweight`, `Normal weight`, `Overweight`, or `Obese` based on the calculated BMI. This task will help you understand how to create new features and classify data based on domain-specific knowledge.

## **Task 5: One-Hot Encoding with Rare Category Handling**
You have a dataset containing a categorical feature `color`. Some categories appear infrequently, which can lead to issues when applying machine learning models. Your task is to group all rare categories (those that appear less than a certain threshold) into a new category called `Other`. Then, perform one-hot encoding on the resulting `color` feature. This task will teach you how to handle rare categories and perform one-hot encoding.


## **Task 6: Target Encoding with Smoothing**
You are provided with a dataset containing a categorical feature `color` and a target variable. Your task is to perform target encoding on the `color` feature, but apply smoothing to account for categories with few observations. Smoothing will help you avoid overfitting to small sample sizes by blending the mean target value of each category with the overall mean. This task introduces you to target encoding and how to apply smoothing to handle small data samples.

