#!/usr/bin/env python3
""" TEST DRIVERS for smoke_v_cancer.py """
from smoke_v_cancer import open_files, read_files 
from nester import nester

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

        
def main():
    # test_open_files()
    test_read_files()
if __name__ == '__main__':
    main()