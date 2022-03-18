"""
Unit tests for the csv combiner 
"""
import sys
import pandas as pd
import csv_combiner as CSVtest
import unittest
from io import StringIO

class TestMethods(unittest.TestCase):

    def testTotalMerge(self):
        accesories = "./fixtures/accessories.csv"
        clothing = "./fixtures/clothing.csv"
        household = "./fixtures/household_cleaners.csv"
        test_path = "./test/test-output.csv"

        output = StringIO()
        sys.stdout = output

        test_output = open(test_path, 'w+')
        argv = ["./csv_combiner.py", accesories,clothing, household]
        CSVtest.fileMerger(argv)
        test_output.write(output.getvalue())
        test_output.close()

        # adding length of all individual files
        accLen = pd.read_csv(filepath_or_buffer=accesories, lineterminator='\n')
        cloLen = pd.read_csv(filepath_or_buffer=clothing, lineterminator='\n')
        hcLen = pd.read_csv(filepath_or_buffer=household, lineterminator='\n')
        sum = len(accLen) + len(cloLen) + len(hcLen)

        # comparing csv file length
        with open(test_path) as f:
            combinedLen = pd.read_csv(filepath_or_buffer=f, lineterminator='\n')
        self.assertEqual(sum, len(combinedLen.drop_duplicates()))

if __name__ == '__main__':
    unittest.main()