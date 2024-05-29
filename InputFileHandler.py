import Coordinate

# Variables
eps = 0

# File Read
def OpenFileHandler(file_address):
    """
        Open file and take the value for x and y axis.

        Parameters:
        file_address(string): Location of input file.
    """
    file1 = open(file_address, "r+")
    print("Output of Read function is ")
    file_input = file1.read()
    print(file_input)
    print()

    ###
    # Check for keys
    # Case of Coordinate as an input
    MatrixInputCheck = file_input.find('Data:matrix')
    if MatrixInputCheck != -1:
        x_array, y_array = Coordinate.extract_coordinate(file_input)

    return x_array, y_array
