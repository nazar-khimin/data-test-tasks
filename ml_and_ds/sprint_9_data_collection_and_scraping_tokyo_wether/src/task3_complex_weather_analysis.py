import json


def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """

    with open(filename, 'r') as f:
        return json.load(f)


def analyze_daily_weather(day, temp_threshold=30, wind_threshold=15, humidity_threshold=70):
    """
    Analyze weather data for a single day.

    Args:
        day (dict): The weather data for the day.
        temp_threshold (float): The temperature threshold to determine a hot day.
        wind_threshold (float): The wind speed threshold to determine a windy day.
        humidity_threshold (float): The humidity threshold to determine uncomfortable weather.

    Returns:
        dict: A dictionary with analysis results for the day.
    """

    return {
        'date': day['date'],
        'temp': {
            'max': day.get('max_temperature', float('-inf')),
            'min': day.get('min_temperature', float('inf')),
        },
        'is_hot_day': day.get('max_temperature', 0) > temp_threshold,
        'temperature_swing': day.get('max_temperature', 0) - day.get('min_temperature', 0),
        'is_windy_day': day.get('wind_speed', 0) > wind_threshold,
        'is_uncomfortable_day': day.get('humidity', 0) > humidity_threshold,
        'precipitation': day.get('precipitation', 0.0),
        'is_rainy_day': day.get('precipitation', 0.0) > 0
    }


def generate_daily_report(analysis):
    """
    Generate a detailed report based on the analysis results for a single day.

    Args:
        analysis (dict): The analysis results for the day.

    Returns:
        str: A detailed report as a string.
    """

    report = f"Date: {analysis['date']}\n"
    report += f"Temperature: Max {analysis['temp']['max']}°C, Min {analysis['temp']['min']}°C\n"
    report += f"{'It was a hot day.' if analysis['is_hot_day'] else ''}\n"
    report += f"{'Significant temperature swing.' if analysis['temperature_swing'] > 10 else ''}\n"
    report += f"{'It was a windy day.' if analysis['is_windy_day'] else ''}\n"
    report += f"{'The humidity made the day uncomfortable.' if analysis['is_uncomfortable_day'] else ''}\n"
    report += f"{'It was a {analysis["rain_severity"]} day.' if analysis['precipitation'] > 0 else 'There was no precipitation.'}\n"
    return report


def summarize_weather_analysis(analyses):
    """
    Summarize the weather analysis over multiple days.

    Args:
        analyses (list of dict): A list of daily analysis results.

    Returns:
        str: A summary report as a string.
    """

    try:
        hottest_day = max(analyses, key=lambda x: x['temp']['max'])
        rainiest_day = max(analyses, key=lambda x: x.get('precipitation', 0))
        windiest_day = max(analyses, key=lambda x: x.get('wind_speed', 0))
        most_humid_day = max(analyses, key=lambda x: x.get('humidity', 0))

        summary = "Weather Summary:\n"
        summary += f"Hottest day: {hottest_day['date']} with a maximum temperature of {hottest_day['temp']['max']}°C\n"
        summary += f"Windiest day: {windiest_day['date']} with wind speed of {windiest_day.get('wind_speed', 0)} km/h\n"
        summary += f"Most humid day: {most_humid_day['date']} with humidity of {most_humid_day.get('humidity', 0)}%\n"
        summary += f"Rainiest day: {rainiest_day['date']} with {rainiest_day.get('precipitation', 0)} mm of precipitation\n"

        return summary
    except KeyError as e:
        return f"Error in analysis data: Missing key {str(e)}"

if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Analyze the weather data for each day
    analyses = [analyze_daily_weather(day) for day in weather_data['daily']]

    # Generate and print daily reports
    for analysis in analyses:
        report = generate_daily_report(analysis)
        print(report)

    # Generate and print a summary report
    summary_report = summarize_weather_analysis(analyses)
    print(summary_report)
