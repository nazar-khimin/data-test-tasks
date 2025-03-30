import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Alice", "Bob", "Charlie", "David", "Alice", "Unknown", "InvalidName"],
    "age": [30, 25, 29, 35, 30, None, 40],  # Missing age
    "department": ["HR", "Finance", "IT", "HR", "HR", "Sales", "UnknownDept"],  # Invalid department
    "salary": [50000, 55000, 60000, 50000, 50000, 70000, 45000]
}

df = pd.DataFrame(data)
df.to_csv("../datasets/anomaly_data.csv", index=False)