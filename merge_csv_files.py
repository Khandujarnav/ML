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
    'labels_06-28-02_06_11_start0.csv',
    'labels_06-28-02_06_11_start300.csv',
    'labels_06-28-02_06_11_start600.csv',
    'labels_06-28-02_06_11_start900.csv',
    'labels_06-28-02_06_11_start1200.csv'
]

# Input the path for the output merged CSV file
output_file_path = 'merged_output.csv'

# Call the function
merge_csv_files(file_paths, output_file_path)
