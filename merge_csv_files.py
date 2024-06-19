import csv

def merge_csv_files(file_paths, output_file_path):
    combined_rows = []
    
    try:
        for file_path in file_paths:
            # Read each CSV file and append its rows to the combined_rows list
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    combined_rows.append(row)
        
        # Write the combined rows to the new output CSV file
        with open(output_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(combined_rows)
                
        print(f"CSV files have been successfully merged into {output_file_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the paths of the CSV files to merge
file_paths = [
    'mapped_snr_1500.csv',
    'mapped_output_2700.csv',
]

# Input the path for the output merged CSV file
output_file_path = 'mapped_snr_4200.csv'

# Call the function
merge_csv_files(file_paths, output_file_path)
