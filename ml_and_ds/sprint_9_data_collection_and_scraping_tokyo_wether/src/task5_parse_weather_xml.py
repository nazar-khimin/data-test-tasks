import xml.etree.ElementTree as ET
import csv


def parse_weather_xml(xml_file):
    """
    Parse weather data from an XML file.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        list of dict: A list of dictionaries with parsed weather data.
    """

    tree = ET.parse(xml_file)
    root = tree.getroot()
    weather_data = []
    for day in root.findall('day'):
        weather_data.append({
            'date': day.find('date').text,
            'temperature': float(day.find('temperature').text),
            'humidity': int(day.find('humidity').text),
            'precipitation': float(day.find('precipitation').text)
        })
    return weather_data


def save_to_csv(data, filename="parsed_weather_data.csv"):
    """
    Save parsed weather data to a CSV file.

    Args:
        data (list of dict): Parsed weather data.
        filename (str): Name of the CSV file.
    """
    if not data:
        print("Error: No data to save")
        return

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["date", "temperature", "humidity", "precipitation"]
        headers = [field.capitalize() for field in fieldnames]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writer.writerow(headers)
        writer.writerows(data)


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully parsed and saved to parsed_weather_data.csv.")
