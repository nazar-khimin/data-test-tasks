from pyspark.sql import functions as F
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler
import numpy as np

def detect_outliers(df, z_threshold=3):
    assembler = VectorAssembler(inputCols=df.columns, outputCol="features")
    df = assembler.transform(df)

    # Calculate the Z-score for each column
    from pyspark.ml.linalg import Vectors
    from pyspark.sql.functions import udf
    from pyspark.sql.types import DoubleType

    def z_score_udf(values):
        mean_val = np.mean(values)
        std_val = np.std(values)
        return [(x - mean_val) / std_val for x in values]

    z_score = udf(z_score_udf, DoubleType())
    df_with_z = df.withColumn("z_score", z_score(F.col("features")))
    df_with_z.show()

def detect_iqr_outliers(df, lower_percentile=0.25, upper_percentile=0.75):
    for col in df.columns:
        q1 = df.approxQuantile(col, [lower_percentile], 0.0)[0]
        q3 = df.approxQuantile(col, [upper_percentile], 0.0)[0]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        print(f"Column: {col} | IQR lower: {lower_bound} | IQR upper: {upper_bound}")