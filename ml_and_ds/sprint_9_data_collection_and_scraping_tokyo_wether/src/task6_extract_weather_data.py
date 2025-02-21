import csv
import re


def clean_text(line):
    """
    Clean the text line by removing non-ASCII characters and fixing known issues.

    Args:
        line (str): The line of text to clean.

    Returns:
        str: The cleaned line of text.
    """
    # Remove non-ASCII characters
    cleaned_line = re.sub(r'[^\x00-\x7F]+', '', line)
    # Replace degree symbol and other special characters
    cleaned_line = cleaned_line.replace('°', '')
    # Remove extra whitespace
    cleaned_line = ' '.join(cleaned_line.split())
    return cleaned_line


def extract_weather_data(text_file):
    """
    Extract weather data from a text file using regular expressions.

    Args:
        text_file (str): Path to the text file.

    Returns:
        list of dict: A list of dictionaries with extracted weather data.
    """
    extracted_data = []
    pattern = r'Date: (\d{4}-\d{2}-\d{2}), Max Temp: ([\d.]+)°?C, Min Temp: ([\d.]+)°?C, Humidity: (\d+)%, Precipitation: ([\d.]+)mm'

    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Clean the line
                cleaned_line = clean_text(line)

                # Skip empty lines
                if not cleaned_line:
                    continue

                # Extract data using regex
                match = re.match(pattern, cleaned_line)
                if match:
                    extracted_data.append({
                        'date': match.group(1),
                        'max_temperature': float(match.group(2)),
                        'min_temperature': float(match.group(3)),
                        'humidity': int(match.group(4)),
                        'precipitation': float(match.group(5))
                    })
    except FileNotFoundError:
        print(f"Error: File {text_file} not found")
        return []
    except UnicodeDecodeError:
        print(f"Error: Unable to decode {text_file}. Please check the file encoding.")
        return []

    return extracted_data


def save_to_csv(data, filename="extracted_weather_data.csv"):
    """
    Save extracted weather data to a CSV file.

    Args:
        data (list of dict): Extracted weather data.
        filename (str): Name of the CSV file.
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Max Temperature', 'Min Temperature',
                      'Humidity', 'Precipitation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        # Convert the data to match the CSV headers
        for row in data:
            writer.writerow({
                'Date': row['date'],
                'Max Temperature': row['max_temperature'],
                'Min Temperature': row['min_temperature'],
                'Humidity': row['humidity'],
                'Precipitation': row['precipitation']
            })


if __name__ == "__main__":
    # Extract data from the text file
    weather_data = extract_weather_data("weather_report.txt")

    # Save the extracted data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully extracted and saved to extracted_weather_data.csv.")
