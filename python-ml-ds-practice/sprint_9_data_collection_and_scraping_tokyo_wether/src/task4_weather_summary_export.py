import json
import csv


def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """

    with open(filename, 'r') as file:
        return json.load(file)


def summarize_weather_data(data):
    """
    Summarize the weather data across all days.

    Args:
        data (list of dict): The daily weather data.

    Returns:
        dict: A summary of the key metrics across all days.
    """

    if not data:
        return {}

    formatted_summary = {
        'hot_days': sum(1 for day in data if day['max_temperature'] > 30),
        'windy_days': sum(1 for day in data if day['wind_speed'] > 15),
        'rainy_days': sum(1 for day in data if day['precipitation'] > 0),
        'average_max_temp': sum(day['max_temperature'] for day in data) / len(data),
        'average_min_temp': sum(day['min_temperature'] for day in data) / len(data),
        'total_precipitation': sum(day['precipitation'] for day in data),
        'average_wind_speed': sum(day['wind_speed'] for day in data) / len(data),
        'average_humidity': sum(day['humidity'] for day in data) / len(data)
    }

    return formatted_summary


def export_to_csv(data, file):
    """
    Export the summarized weather data to a CSV file or file-like object.

    Args:
        data (list of dict): The daily weather data to export.
        file (str or file-like object): The name of the CSV file to save the data in, or a file-like object.
    """
    fieldnames = ['Date', 'Max Temperature', 'Min Temperature', 'Precipitation',
                  'Wind Speed', 'Humidity', 'Weather Description', 'Is Hot Day',
                  'Is Windy Day', 'Is Rainy Day']

    try:
        if isinstance(file, str):
            with open(file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
        else:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        for entry in data:
            entry["Is Hot Day"] = "True" if entry["max_temperature"] > 30 else "False"
            entry["Is Windy Day"] = "True" if entry["wind_speed"] > 10 else "False"
            entry["Is Rainy Day"] = "True" if entry["precipitation"] > 0 else "False"

            writer.writerow({
                'Date': entry["date"],
                'Max Temperature': entry["max_temperature"],
                'Min Temperature': entry["min_temperature"],
                'Precipitation': entry["precipitation"],
                'Wind Speed': entry["wind_speed"],
                'Humidity': entry["humidity"],
                'Weather Description': entry["weather_description"],
                'Is Hot Day': entry["Is Hot Day"],
                'Is Windy Day': entry["Is Windy Day"],
                'Is Rainy Day': entry["Is Rainy Day"]
            })
    except IOError:
        raise IOError(f"Error writing to file: {file}")


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Summarize the weather data
    summary = summarize_weather_data(weather_data['daily'])

    # Print the summary for verification
    print("Weather Data Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export the summarized data to a CSV file
    export_to_csv(weather_data['daily'], "tokyo_weather_summary.csv")

    print("Data successfully exported to tokyo_weather_summary.csv")
