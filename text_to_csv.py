import csv

def convert_txt_to_csv():
    txt_file_path = 'labels_06-28-02_06_11_start1200.txt'
    csv_file_path = txt_file_path.rsplit('.', 1)[0] + '.csv'
    
    try:
        with open(txt_file_path, 'r') as txt_file:
            lines = txt_file.readlines()
        
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            for line in lines:
                # Split the line into components and convert to float
                float_values = [float(value) for value in line.split()]
                # Write the float values as a row in the CSV
                csv_writer.writerow(float_values)
                
        print(f"Data successfully converted from {txt_file_path} to {csv_file_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
convert_txt_to_csv()
