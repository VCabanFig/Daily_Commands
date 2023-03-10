#!/usr/bin/env python
import os

# Get the current working directory
current_directory = os.getcwd()

# Set the path for the directory with the text files
text_directory = os.path.join(current_directory, 'text_files')

# Set the path for the directory where the CSV files will be saved
csv_directory = os.path.join(current_directory, 'csv_files')

# Loop through all files in the text directory
for filename in os.listdir(text_directory):
    if filename.endswith('.txt'):
        # Set the path for the current text file
        text_file_path = os.path.join(text_directory, filename)

        # Set the path for the corresponding CSV file
        csv_file_path = os.path.join(csv_directory, filename[:-4] + '.csv')

        # Open the text file for reading and the CSV file for writing
        with open(text_file_path, 'r') as text_file, open(csv_file_path, 'w') as csv_file:
            # Loop through each line in the text file
            for line in text_file:
                # Split the line into columns using commas as the delimiter
                columns = line.strip().split(',')

                # Write the columns to the CSV file
                csv_file.write(','.join(columns) + '\n')
