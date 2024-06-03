Assignment: 
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

The code is divided into 3 modules:
Main, number_helper and mean_var_std_helper.
The main module calls for the various functions and prints the results as required by the assignment.
The mean_var_std_helper module contains the main function (calculate()). 
This function takes the list of numbers obtained by the get_number() function in the number_helper module as argument.
The calculate() function returns a dictionary with the required names of the various descriptive statistical methods as keys 
and the list of the results (eg mean of each of the three columns, mean of each of the three rows and overall mean
