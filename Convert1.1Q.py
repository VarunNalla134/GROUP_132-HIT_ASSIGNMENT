import csv
import os

# Get a list of all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Open a text file to write the extracted text to
with open('output.txt', 'w') as f:
    # Loop through each CSV file
    for csv_file in csv_files:
        # Open the CSV file and read its contents
        with open(csv_file, 'r') as csv_file_obj:
            # Get the CSV reader object
            csv_reader = csv.reader(csv_file_obj)

            # Loop through each row in the CSV file
            for row in csv_reader:
                # Write the row's text to the text file
                f.write(' '.join(row) + '\n')