def analyze_scores(scores):
    # Check if the dictionary is empty
    if not scores:
        return {
            'average_score': None,
            'top_students': [],
            'highest_scorer': None
        }

    # Calculate the average score
    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    average_score = round(average_score, 1)

    # Identify the top scorers (students with score >= 90)
    top_students = [name for name, score in scores.items() if score >= 90]

    # Find the student with the highest score
    highest_scorer = max(scores, key=scores.get)

    # Return the results
    return {
        'average_score': average_score,
        'top_students': top_students,
        'highest_scorer': highest_scorer
    }


# Example usage:
scores = {"Олег": 85, "Анна": 92, "Марія": 78, "Іван": 90}
result = analyze_scores(scores)
print(result)

scores = {}
result = analyze_scores(scores)
print(result)