#!/usr/bin/env python3
""" TEST DRIVERS for smoke_v_cancer.py """
from smoke_v_cancer import open_files, read_files, calculate_correlation

def test_open_files():
    """ TEST DRIVER for open_files() """
    empty_str = ''
    print('TESTING FUNCTION smoke_v_cancer.open_files()')
    try:
        smoking_data_file, cancer_data_file = open_files()      # open data files
        print('Data files successfully opened')                 # Display successfully opened
        print('\nReading first line of smoking data file ...')
        line = smoking_data_file.readline()
        print(line.strip('\n'))                                 # Display first line of smoking data file
        print('\nReading first line of cancer data file ...')
        line = cancer_data_file.readline()                      
        print(line.strip('\n'))                                 # Display first line of cancer data file
    except IOError:
        print('Too many attempts of opening input files')
        print('Program Terminated')

def test_read_files():
    """ TEST DRIVER for smoke_v_cancer.read_files() """
    try:
        # Open Smoking and Cancer rate data files
        smoking_data_file, cancer_data_file = open_files()
        # Read file data
        smoking_data, cancer_data = read_files(
            smoking_data_file, cancer_data_file)

        print(format(' Smoking-Tings ', '*^80'))
        print(smoking_data)
        print(format(' Cancer-Ting ', '*^80'))
        print(cancer_data)
    except IOError as ioerr:
        print('Oops... : {0}'.format(ioerr))

def test_calculate_correlation():
    """ TEST DRIVER for calculate_correlation() """
    # Calculate perfect positive correlation
    print('Calculating perfect positive correlation ...')
    smoking_data = [['A', 10], ['B', 20], ['C', 30], ['D', 40]]
    cancer_data = [['A', 100], ['B', 200], ['C', 300], ['D', 400]]
    print('Correlation value: {0}'.format(calculate_correlation(smoking_data, cancer_data)))
    
    # Calculate perfect Zero correlation
    print('\nCalculating perfect negative correlation ...')
    smoking_data = [['A', 10], ['B', 20], ['C', 30], ['D', 40]]
    cancer_data = [['A', 100], ['B', 0], ['C', 300], ['D', 0]]
    print('Correlation value: {0}'.format(calculate_correlation(smoking_data, cancer_data)))

    # Calculate perfect negative correlation
    print('\nCalculating perfect negative correlation ...')
    smoking_data = [['A', 10], ['B', 20], ['C', 30], ['D', 40]]
    cancer_data = [['A', 400], ['B', 300], ['C', 200], ['D', 100]]
    print('Correlation value: {0}'.format(calculate_correlation(smoking_data, cancer_data)))
        
def main():
    # test_open_files()
    # test_read_files()
    test_calculate_correlation()

if __name__ == '__main__':
    main()