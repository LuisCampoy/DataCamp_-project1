# Data Analysis with Python: DataCamp.org
# Project #1: Mean_Variance_Standard_Deviation Calculator
# function module
# Script Started 5/31/2024
# Last Revision 5/31/2024

import numpy as np

def calculate(numbers: list) -> dict:
    
    """ This function calculates basic descriptive statistical methods such mean, sd, variance, min, max and sum
        across rows, columns and altogether and stores the results in a dictionary with the name of the
        test as a key

    Args:
        numbers: list of numbers entered by the user

    Returns:
        list of float values
    """
       
    # Convert list to 3x3 Numpy array
    array: np.array = np.array(numbers).reshape(3, 3)
    
    calculations: dict = {
        'mean': [
            np.mean(array, axis=0).tolist(),  # Mean of columns (axis 0)
            np.mean(array, axis=1).tolist(),  # Mean of rows (axis 1)
            np.mean(array).tolist()           # Mean of all elements
        ],
        'variance': [
            np.var(array, axis=0).tolist(),   # Variance of columns
            np.var(array, axis=1).tolist(),   # Variance of rows
            np.var(array).tolist()            # Variance of all elements
        ],
        'standard deviation': [
            np.std(array, axis=0).tolist(),   # Standard deviation of columns
            np.std(array, axis=1).tolist(),   # Standard deviation of rows
            np.std(array).tolist()            # Standard deviation of all elements
        ],
        'max': [
            np.max(array, axis=0).tolist(),   # Max of columns
            np.max(array, axis=1).tolist(),   # Max of rows
            np.max(array).tolist()            # Max of all elements
        ],
        'min': [
            np.min(array, axis=0).tolist(),   # Min of columns
            np.min(array, axis=1).tolist(),   # Min of rows
            np.min(array).tolist()            # Min of all elements
        ],
        'sum': [
            np.sum(array, axis=0).tolist(),   # Sum of columns
            np.sum(array, axis=1).tolist(),   # Sum of rows
            np.sum(array).tolist()            # Sum of all elements
        ]
    }
    
    return calculations
