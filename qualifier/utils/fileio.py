# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, csv_data_list):
    """
    Writes a rate_sheet csv file to location specified by csvpath.

    Args:
        csvpath (Path) the csv file path to write to
        csv_data_list (list) of bank rate sheet entries. each item in the list is
            a list matching the following ordering/format six items:
                Lender,Max Loan Amount,Max LTV,Max DTI,Min Credit Score,Interest Rate
    
    Returns: nothing is explicitly returned. A csv file is written to disk.

    """
    csv_header = "Lender,Max Loan Amount,Max LTV,Max DTI,Min Credit Score,Interest Rate".split(',')
    with open(csvpath, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_header)
        writer.writerows(csv_data_list)
