import os
import sys
import pandas as pd

def fileValidator(files):
    """
    Function that checks if files are valid, else it will output the error and
    end the program

    Parameters
    ----------
    List of CSV files passed by the user
    """
    if len(files) <= 1:
        print("Error, incorrect number of arguments passed in")
        return False
    
    for filepath in files:
        if not os.path.exists(filepath):
            print("Error, one of the files does not exist")
            return False
    return True

def fileMerger(argv: list):
    """
    Function that takes several CSV files as arguments and outputs a new CSV file to 
    `stdout` that contains the rows from each of the inputs along with an additional
    column that has the filename from which the row came.

    Parameters
    ----------
    Arguments passed in by the user
    """
    # using chunks to prevent memory issues with larger files
    chunkSize = 50000
    chunks = []
    files = argv[1:]
    
    if fileValidator(files):
        header = True
        for filepath in files:
            for chunk in pd.read_csv(filepath, chunksize=chunkSize):
                filename = os.path.basename(filepath)
                chunk['filename'] = filename
                chunks.append(chunk)
        
        for chunk in chunks:
            print(chunk.to_csv(header = header, index=False, chunksize=chunkSize, line_terminator='\n'), end='')
            header = False

    else:
        return

if __name__ == '__main__':
    fileMerger(sys.argv)