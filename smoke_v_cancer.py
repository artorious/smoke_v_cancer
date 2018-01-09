#!/usr/bin/env python3
"""Cigarette Use/Lung Cancer Correlation Program 

Calculates a correlation value for two sets of data.
Correlation is measured on  a scale of  -1 to 1, with 1 indicating a
perfect positive correlation, and -1 a perfect negative correlation.

NOTE: Example Analogy
    There is a positive correlation between the amount of ice cream sold and the 
    current temperature - as temperatures rise, so do the sales of ice cream. 
    
    There is a negative correlation between the number of snow blowers sold and 
    the current temperature — as temperatures rise, the number of snow blowers 
    sold decreases.
    
    In a perfect correlation, knowing one value allows one to determine the exact 
    value of the other.
    In real-world situations, perfect correlations are almost never found. 
    For example, many other factors can affect exactly how much ice cream is 
    sold — there may be a truckers’ strike reducing deliveries, there may be a 
    recall of a certain brand of ice cream, and so forth. 
    Therefore, most correlation values fall somewhere between -1 and 1.
"""

### PROBLEM ANALYSIS
# The two sets of data provided contain;
#   - Percentage of the population that smokes, state-by-state
#   - State-by-state rates of incidence of lung cancer per 100,000 individuals
#
# Using The Mathematical formula for computing correlation on the provided data;
#   N -> 48 (all states except Arizona & Wisconsin whose data is not provided)
#   x and y values -> the percent of population that smokes and lung cancer cases per 100,000 individuals
#       Example x and y values for Alabama, (x=23.3) and (y=75.1)
# NOTE: To apply this formula, the values of x and y do not have to be in the same units

### PROGRAM DESIGN
# Data is provided in  two comma-separated (CSV) files.
# TODO:   
#   -> Read the data from csv files
#   -> Using this data, compute the correlation of the two sets of data in a scale of 
#       -1 (a perfect negative correlation) to 1 (a perfect positive correlation)

### Meeting the Program Requirements
# The program must only display the correlation value between the two sets of data.
# The raw numerical value will simply be dispalyed on the screen

### Data Description
# Store data from files in two corresponding 'parallel' lists of floating-point values
# for easiy access during calculation of correlation
#---------------------------------------------------------------------------------------------

# TODO:
# Import Math Module -> Calculate correlation
#------------------------------------------------------

def open_files():
    """ () -> tuple
    Prompts user for file names and opens the files.
    Returns tuple of file objects, (smoking_data_file, cancer_data_file)
    Raises an IOError exception if the files are not successfully opened
    after four attempts of entering file names
    """
    # Init controls for loop that continually prompt the user until correct 
    # file names for the data files are entered (4 Attempts).
    smoking_data_file_opened = False
    cancer_data_file_opened = False
    num_attempts = 4

    # prompt for file names and attempt to open files
    while ((not smoking_data_file_opened) or (not cancer_data_file_opened)) \
            and (num_attempts > 0):
        
        try:
            if not smoking_data_file_opened:
                file_name = input('Enter smoking data file name: ')
                smoking_data_file = open(file_name, 'r')
                smoking_data_file_opened = True
          
            if not cancer_data_file_opened:
                file_name = input('Enter lung cancer data file name: ')
                cancer_data_file = open(file_name, 'r')
                cancer_data_file_opened = True
        
        except IOError as ioerr:
            print('File not found:{0} - Try again\n'.format(file_name))
            num_attempts -= 1
    
    # If one or more file not opened, raise IOError exception
    if not smoking_data_file_opened or not cancer_data_file_opened:
        raise IOError('one or more file not opened')
    
    else:
        return (smoking_data_file, cancer_data_file)

def read_files(smoking_data_file, cancer_data_file):
    """
    Read file data
    Return 
    """
    pass

def calculate_correlation(smoking_data, cancer_data):
    """ (list, list) -> int
    Calculate correlation
    """
    pass
    

def main():
    """Cigarette Use/Lung Cancer Correlation Program 
    
    Module utilizes three functions;
        open_files()
        read_files()
        calculate_correlation()
    """

    try:
        # Program Greeting
        print(''' 
        This program will determine the correlation between
        cigarette smoking and incidences of lung cancer.
        ''')
        # Open Smoking and Cancer rate data files
        smoking_data_file, cancer_data_file = open_files()
        # Read file data
        smoking_data, cancer_data = read_files(
            smoking_data_file, cancer_data_file)
        # Calculate correlation
        correlation = calculate_correlation(smoking_data, cancer_data)
        # Display correlation value
        print('r_value = {0}'.format(correlation))
    except IOError as ioerr:
        print('Ooops....: {0}'.format(ioerr))

if __name__ == '__main__':
    main()


 

