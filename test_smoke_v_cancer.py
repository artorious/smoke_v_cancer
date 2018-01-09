#!/usr/bin/env python3
""" TEST DRIVERS for smoke_v_cancer.py """
from smoke_v_cancer import open_files 

def test_open_files():
    """ TEST DRIVER for open_files() """
    empty_str = ''
    print('TESTING FUNCTION open_files()')

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

def main():
    test_open_files()

if __name__ == '__main__':
    main()