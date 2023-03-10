
#!/usr/bin/env python


import os
import pandas as pd
import csv

# Set the directory path where CSV files are

csv_dir ='path/to/directory/where/csv/files/are/located'

# Set the path to the directory containing the csv files


# Set the path and filename for the output Excel file
output_file = 'merged_file.xlsx'

# Get a list of all csv files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

# Create a Pandas Excel writer object to write the concatenated data to an Excel file
writer = pd.ExcelWriter(output_file, engine='openpyxl')

# Loop through each csv file, read it into a Pandas DataFrame, and write it to a new sheet in the Excel file
for csv_file in csv_files:
    sheet_name = os.path.splitext(csv_file)[0]  # Use the csv file name as the sheet name
    df = pd.read_csv(os.path.join(csv_dir, csv_file), quoting=csv.QUOTE_ALL, error_bad_lines=False)
    df.to_excel(writer, sheet_name=sheet_name, index=False)


# Save the Excel file and close the writer object
writer.save()
writer.close()

print(f'Concatenated {len(csv_files)} csv files to {output_file}')
