# Data Analysis with Python: DataCamp.org
# Project #1: Mean_Variance_Standard_Deviation Calculator
# number_helper module
# Script Started 5/31/2024
# Last Revision 5/31/2024

def get_numbers() -> list:
    
    """ Obtain 9 numbers entered by user. This function uses a while loop and uses function len()
        to count. it adds 1 because of 0 indexing.
        Each number is the added to the numbers list.

    Args:
        none

    Returns:
        list of float values
    """
    
    numbers: list = []
    
    while len(numbers) < 9:
        try:
            num = float(input(f'Enter number {len(numbers) +1}: '))
            numbers.append(num)
            
        except ValueError:
            print('Not sure that was a number...')
    
    if len(numbers) != 9:
        raise ValueError('List must contain nine numbers...')
    
    return numbers