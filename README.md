# Wine Quality Data Quality Validation

This project demonstrates automated **data quality validation, profiling, anomaly detection, and root cause analysis** using **PySpark** and the **Wine Quality Dataset**. The goal is to showcase **data integrity checks, ETL validation, and data monitoring** in a real-world scenario.

## 📌 Features

### **1️⃣ Data Quality Validation**
- Schema validation
- Null value detection
- Duplicate record checks
- Range and threshold validation

### **2️⃣ Data Profiling & Anomaly Detection**
- Descriptive statistics
- Outlier detection (Z-score, IQR)

### **3️⃣ ETL Validation**
- Pre-ETL data quality checks
- Post-ETL data validation
- Transformation verification

### **4️⃣ SQL Data Integrity Checks**
- Referential integrity validation
- Business rule enforcement
- Historical data consistency

### **5️⃣ Root Cause Analysis & Monitoring**
- Logging & error tracking
- Data lineage tracing
- Pipeline monitoring

---
## 📊 Dataset: Wine Quality Dataset

I use the [Wine Quality Dataset](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset/data), introducing **synthetic anomalies** (missing values, duplicates, outliers) for testing purposes.

---
## 🚀 Setup & Installation

```sh
# Clone the repository
git clone https://github.com/your-username/pyspark-wine-data-quality.git
cd pyspark-wine-data-quality

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---
## 📂 Project Structure
```
pyspark-wine-data-quality/
│── README.md
│── projects/
│   │── data_quality_validation/
│   │── data_profiling/
│   │── etl_data_validation/
│   │── sql_data_validation/
│   │── root_cause_analysis/
│── datasets/
│── notebooks/
│── docs/
│── .github/workflows/
│── LICENSE
```
---
## 📋 Running the Project

### **1️⃣ Run Data Quality Validation**
```sh
spark-submit projects/data_quality_validation/main.py
```

### **2️⃣ Run Tests**
```sh
pytest tests/
```

---
## 📝 Notebooks for Interactive Analysis
- **data_quality_checks.ipynb** – Schema validation, null checks, duplicate detection
- **etl_validation.ipynb** – Pre/post-ETL validation
- **profiling_analysis.ipynb** – Statistical profiling & anomaly detection