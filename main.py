# Data Analysis with Python: 
# Project #1: Mean_Variance_Standard_Deviation Calculator
# main script
# Script Started 5/31/2024
# Last Revision 5/31/2024

''' 
Assignement: 
Create a function named calculate() in mean_var_std.py that uses Numpy 
to output the mean, variance, standard deviation, max, min, and sum 
of the rows, columns, and elements in a 3 x 3 array.
The input of the function should be a list containing 9 digits. 
The function should convert the list into a 3 x 3 Numpy array, 
and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum 
along both axes and for the flattened array.
If a list containing less than 9 elements is passed into the function, 
it should raise a ValueError exception with the message: "List must contain nine numbers." 
The values in the returned dictionary should be lists and not Numpy arrays.
'''

from mean_var_std import calculate
from number_helper import get_numbers

def main() -> None:
    
    numbers: list = get_numbers()
    
    #numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    calculations = calculate(numbers)
    
    print(f"'mean': {calculations['mean'][0:3]},")
    print(f"'variance': {calculations['variance'][0:3]},")
    print(f"'standard deviation': {calculations['standard deviation'][0:3]},")
    print(f"'max': {calculations['max'][0:3]},")
    print(f"'min': {calculations['min'][0:3]},")
    print(f"'sum': {calculations['sum'][0:3]}")
        
if __name__ == "__main__":
    
    main()