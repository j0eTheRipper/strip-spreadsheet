from strip_spreadsheet import clean_sheet
from name_new_sheet import name_file
import argparse


# parse the arguments.
arguments = argparse.ArgumentParser()

arguments.add_argument('spreadsheet', help='Path to the unclean spreadsheet.')
arguments.add_argument('-o', '--output_sheet', help='Path to where the new, clean sheet is going to be.')

arguments = arguments.parse_args()

# modify the given sheet
with open(arguments.spreadsheet) as csv_file:
    unclean_spreadsheet = csv_file.readlines()
    clean_spreadsheet_name = name_file(arguments.spreadsheet, arguments.output_sheet)

    with open(clean_spreadsheet_name, 'w') as new_csv_file:
        clean_spreadsheet = clean_sheet(unclean_spreadsheet)
        new_csv_file.writelines(clean_spreadsheet)
