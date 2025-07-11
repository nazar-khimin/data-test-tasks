"""
This module contains the Spark tasks.
"""
import csv
from pyspark import SparkContext, RDD
from typing import Literal


def load_dataset(sc: SparkContext, file_path: str, wine_type: str) -> RDD:
    """
    Load the dataset, clean it, and add wine type as an additional column.
    
    Args:
        sc (SparkContext): The SparkContext for distributed computation.
        file_path (str): Path to the dataset file (CSV format).
        wine_type (str): The type of wine (e.g., "red" or "white").
        
    Returns:
        RDD: An RDD where each row is a list representing a wine record, 
        with the wine type appended as the last element.
    
    Process:
        - Read the dataset from the given file path.
        - Remove the header row to avoid processing metadata.
        - Split each row into a list of values using the delimiter.
        - Append the wine type (red/white) to each record.
    """
    raw_rdd = sc.textFile(file_path)
    header = raw_rdd.first()
    delimeter = detect_delimiter_from_string(header)
    data_rdd = raw_rdd.filter(lambda line: line != header)
    rdd_split = data_rdd.map(lambda line: line.split(delimeter))
    rdd_with_type = rdd_split.map(lambda record: record + [wine_type])
    return rdd_with_type

def detect_delimiter_from_string(sample_string):
    sniffer = csv.Sniffer()
    return sniffer.sniff(sample_string).delimiter

def filter_wines_by_quality(data_rdd: RDD, quality_threshold: int,
                            comparator: Literal["gte", "lte"]) -> RDD:
    """
    Filter wines based on a quality threshold and a comparison operator.
    
    Args:
        data_rdd (RDD): Input RDD where each record represents a wine and includes a quality score.
        quality_threshold (int): The quality score threshold for filtering.
        comparator (Literal["gte", "lte"]): The comparison operator:
            - "gte": Include wines with quality greater than or equal to the threshold.
            - "lte": Include wines with quality less than or equal to the threshold.
    
    Returns:
        RDD: Filtered RDD containing only records that meet the specified condition.
    
    Raises:
        ValueError: If an invalid comparator is provided.
    
    Process:
        - Filter records based on the quality score column.
        - Implement "greater than or equal to" and "less than or equal to" comparisons.
        - Throw 'ValueError' if comparator is not a supported value.
    """
    quality_index = 11
    if comparator == "gte":
        return data_rdd.filter(lambda record: int(record[quality_index]) >= quality_threshold)
    elif comparator == "lte":
        return data_rdd.filter(lambda record: int(record[quality_index]) <= quality_threshold)
    else:
        raise ValueError("Invalid comparator. Use 'gte' or 'lte'.")

def compute_average_feature(data_rdd: RDD, feature_index: int) -> float:
    """
    Compute the average value of a specified feature.
    
    Args:
        data_rdd (RDD): Input RDD where each record represents a wine.
        feature_index (int): The index of the feature (column) to average.
    
    Returns:
        float: The average value of the specified feature. Returns 0.0 if no records exist.
    
    Process:
        - Extract the specified feature column.
        - Use aggregate operations to calculate the total sum and count of values.
        - Compute the average as the total divided by the count.
    """

    def partOp(acc: tuple[int, float], x: int | float) -> tuple[int, float]:
        """
        Accumulates the count and sum for a single partition.
        
        Args:
            acc (tuple[int, float]): Current accumulator state:
                - acc[0]: Count of elements.
                - acc[1]: Sum of elements.
            x (float): The value to add to the accumulator.
        
        Returns:
            tuple[int, float]: Updated accumulator state.
        """
        count, total_sum = acc
        return count + 1, total_sum + x

    def totalOp(acc1: tuple[int, float], acc2: tuple[int, float]) -> tuple[int, float]:
        """
        Combines accumulator results from different partitions.
        
        Args:
            acc1 (tuple[int, float]): First accumulator state.
            acc2 (tuple[int, float]): Second accumulator state.
        
        Returns:
            tuple[int, float]: Combined accumulator state.
        """
        count1, total_sum1 = acc1
        count2, total_sum2 = acc2
        return count1 + count2, total_sum1 + total_sum2

    feature_rdd = data_rdd.map(lambda record: float(record[feature_index]))
    count, total_sum = feature_rdd.aggregate((0, 0.0), partOp, totalOp)
    return total_sum / count if count != 0 else 0.0

def quality_distribution(data_rdd: RDD) -> RDD:
    """
    Calculate the distribution of wines by quality score.
    
    Args:
        data_rdd (RDD): Input RDD where each record represents a wine and includes a quality score.
    
    Returns:
        RDD: An RDD of key-value pairs where:
            - Key: Quality score (int).
            - Value: Count of wines with that quality score (int).
    
    Process:
        - Map each record to a (quality, 1) key-value pair.
        - Aggregate counts for each quality score.
    """
    quality_index = 11
    return data_rdd.map(lambda record: (int(record[quality_index]), 1)).reduceByKey(lambda x, y: x + y)

def compute_analysis_by_type(data_rdd: RDD) -> RDD:
    """
    Perform an analysis of average alcohol content grouped by wine type.
    
    Args:
        data_rdd (RDD): Input RDD where each record represents a wine and includes the wine type.
    
    Returns:
        RDD: An RDD of key-value pairs where:
            - Key: Wine type (str, e.g., "red" or "white").
            - Value: Average alcohol content (float) for that type.
    
    Process:
        - Map each record to a (wine_type, (1, alcohol_content)) key-value pair.
        - Aggregate counts and total alcohol content for each wine type using.
        - Compute the average alcohol content as total alcohol divided by count for each type.
    """
    type_index = 12
    alcohol_index = 10

    type_rdd = data_rdd.map(lambda record: (record[type_index], (1, float(record[alcohol_index]))))
    aggregated = type_rdd.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
    return aggregated.mapValues(lambda value: value[1] / value[0])

def save_rdd_to_file(rdd: RDD, output_path: str) -> None:
    """
    Save the contents of an RDD to a text file.
    
    Args:
        rdd (RDD): Input RDD containing the data to save.
        output_path (str): Path to the output directory where the file will be saved.
    
    Process:
        - Convert each RDD record into a string representation 'key: value'.
        - Save the records as a text file in the specified output directory.
    """
    rdd.map(lambda record: f"{record[0]}: {record[1]}").saveAsTextFile(output_path)
