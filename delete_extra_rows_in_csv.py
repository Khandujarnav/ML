import csv

def trim_csv_file():
    csv_file_path = 'labels_06-28-02_06_11_start5700.csv'
    
    try:
        # Read the existing CSV file
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        
        # Trim the rows to the first 300
        trimmed_rows = rows[:300]
        
        # Write the trimmed rows back to the CSV file
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(trimmed_rows)
                
        print(f"CSV file at {csv_file_path} has been trimmed to the first 300 rows.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
trim_csv_file()
