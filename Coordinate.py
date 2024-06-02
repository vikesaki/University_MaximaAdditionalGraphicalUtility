import math

import numpy as np
import re


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


def add_boundaries(xArray, yArray, value):
    """
    Adding Boundaries to the x and y coordinate
    :param value: float value of x boundaries
    :param xArray:
    :param yArray:
    :return: x_array, y_array
    """

    value = float(value)
    new_x = np.max(xArray) + value
    # new_y = math.floor(yArray.min())

    # Prepend the new value to the array
    xArray = np.insert(xArray, 0, new_x)
    xArray = np.append(xArray, 0)
    for i in range(2):
        yArray = np.insert(yArray, 0, 0)

    return xArray, yArray


def duplicate_coordinates(x_array, y_array):
    """
    Duplicate the coordinates (x, y values) in the input arrays.
    Parameters:
    x_array (numpy.ndarray): Array of x values.
    y_array (numpy.ndarray): Array of y values.
    Returns:
    numpy.ndarray, numpy.ndarray: Arrays containing duplicated coordinates, sorted in descending order.
    """
    assert len(x_array) == len(y_array), "x_array and y_array must have the same length."

    duplicated_x = np.repeat(x_array, 2)  # Duplicate each x value
    duplicated_y = np.repeat(y_array, 2)  # Duplicate each y value

    duplicated_x = np.sort(duplicated_x)[::-1]

    return duplicated_x, duplicated_y
