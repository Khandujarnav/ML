import csv

def drop_first_column(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = [row[1:] for row in csv_reader]  # Remove the first column from each row
        
        with open(output_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(rows)
                
        print(f"First column successfully removed and new file saved as {output_file_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output file paths
input_file_path = 'labels_06-28-02_06_11_start5700.csv'
output_file_path = 'output_without_first_column_test_5700.csv'

# Call the function
drop_first_column(input_file_path, output_file_path)
