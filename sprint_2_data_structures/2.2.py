def analyze_visits(visits: list[int]) -> dict:
    # Total number of visitors for the month
    total_visits = sum(visits)

    # Average number of visitors per day, rounded to 2 decimal places
    if len(visits) > 0:
        avg_visits = round(total_visits / len(visits), 2)
    else:
        avg_visits = 0.0  # Handle case of an empty list

    # Maximum number of visitors per day
    max_visits = max(visits) if visits else 0  # Handle case of empty list

    # Number of days with visits (non-zero values)
    days_with_visits = len([day for day in visits if day > 0])

    # Return the analysis as a dictionary with expected key names
    return {
        'total_visits': total_visits,
        'avg_visits': avg_visits,
        'max_visits': max_visits,
        'days_with_visits': days_with_visits
    }


# Example usage:
visits = [12, 15, 0, 3, 7, 8, 0, 10, 6]
result = analyze_visits(visits)
print('Result 1:', result)  # {'total_visits': 61, 'avg_visits': 6.78, 'max_visits': 15, 'days_with_visits': 7}

visits = [0, 0, 0, 0]
result = analyze_visits(visits)
print('Result 2:', result)  # {'total_visits': 0, 'avg_visits': 0.0, 'max_visits': 0, 'days_with_visits': 0}

visits = [5, 10, 15]
result = analyze_visits(visits)
print('Result 3:', result)  # {'total_visits': 30, 'avg_visits': 10.0, 'max_visits': 15, 'days_with_visits': 3}

visits = [8]
result = analyze_visits(visits)
print('Result 3:', result)  # {'total_visits': 8, 'avg_visits': 8.0, 'max_visits': 8, 'days_with_visits': 1}