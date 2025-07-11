import re


def max_population(data):
    # Regular expression to capture the name and population from the data lines
    pattern = re.compile(r"(\w+_\w+),(\d+),(\w)")  # Match name, population, and capital flag

    max_pop = 0
    max_location = ""

    # Iterate through each line in the input data (skip the header)
    for line in data[1:]:  # Skip the header (first line)
        line = line.strip()  # Remove any leading or trailing spaces
        match = pattern.match(line)  # Match each line against the regex
        if match:
            name = match.group(1)  # Extract the location name
            population = int(match.group(2))  # Convert population to integer

            print(f"Processing: {name} with population {population}")  # Debugging print

            # Update the maximum population and location if necessary
            if population > max_pop:
                max_pop = population
                max_location = name

    # Return the location with the highest population and its population
    return (max_location, max_pop)


# Example usage
data = [
    "id,name,poppulation,is_capital",
    "3024,eu_kyiv,24834,y",
    "3025,eu_volynia,20231,n",
    "3026,eu_galych,23745,n",
    "4892,me_medina,18038,n",
    "4401,af_cairo,18946,y",
    "4700,me_tabriz,13421,n",
    "4899,me_bagdad,22723,y",
    "6600,af_zulu,09720,n"
]

print(max_population(data))  # Expected output: ('eu_kyiv', 24834)