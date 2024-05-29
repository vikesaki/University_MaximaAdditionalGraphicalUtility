import re
import numpy as np

def extract_coordinate(input_string):
    """
    Extract the coordinate from the input
    :param input_string: text with the form of [num,num]
    :return: x_array, y_array
    """

    # Regex pattern to match each pair of values, including scientific notation
    pattern = r'\[([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?),([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\]'

    matches = re.findall(pattern, input_string)

    x_values = []
    y_values = []

    for match in matches:
        x_values.append(float(match[0]))
        y_values.append(float(match[1]))

    # Convert lists to numpy arrays
    x_array = np.array(x_values)
    y_array = np.array(y_values)

    return x_array, y_array

# Example input string
input_string = "Data:matrix([0,0.0126122],[7.36856E-4,-0.011544],[6.41314E-4,-0.0116698],[6.81314E-4,-0.00294088],[4.0E-4,-0.00301193],[7.5E-4,0],[7.5E-4,0.0113269]);"

# Extract coordinates
x_array, y_array = extract_coordinate(input_string)

print("x_array:", x_array)
print("y_array:", y_array)