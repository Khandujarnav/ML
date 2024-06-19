#code to map snr values to inout file and fill the snr values with random values b/w range 21.4-22.5 for the remaining data

import pandas as pd
import numpy as np

# Paths to the input files
input_file = 'input_test_5700-6000.csv'  # Update with the correct path
snr_file = 'output_without_first_column_test_5700.csv'  # Update with the correct path
output_file = 'mapped_output_5700.csv'

# Read the input file (CSV with 0 and 1 values)
input_data = pd.read_csv(input_file, header=None, dtype=int)

# Read the SNR file (CSV with SNR values)
def read_snr_file(filepath):
    snr_data = []
    with open(filepath, 'r') as file:
        for line in file:
            snr_values = line.strip().split(',')
            snr_values = [float(value) for value in snr_values if value]  # Convert to float and filter out empty values
            snr_data.append(snr_values)
    return snr_data

# Read the SNR file using the custom function
snr_data = read_snr_file(snr_file)
# Initialize the array to store mapped SNR values
mapped_snr_data = []

# Determine the number of rows to process based on the smaller of the two files
num_rows_to_process = min(len(input_data), len(snr_data))

# Process each row up to the number of SNR rows available
for index in range(num_rows_to_process):
    # Create a zero array of length 80
    mapped_row = np.zeros(80)
    
    # Get the corresponding SNR values for this row
    snr_values = snr_data[index]
    
    # Ensure the number of SNR values matches the number of '1's in the input row
    row = input_data.iloc[index].values
    num_ones = sum(row)
    if len(snr_values) != num_ones:
        print(f"Row {index}: Number of '1's in input row ({num_ones}) does not match number of SNR values ({len(snr_values)})")
        continue  # Skip this row or handle the mismatch appropriately
    
    # Map the SNR values to the positions where input_data is 1
    snr_index = 0
    for i, val in enumerate(row):
        if val == 1:
            mapped_row[i] = snr_values[snr_index]
            snr_index += 1
    
    # Append the mapped row to the list
    mapped_snr_data.append(mapped_row)
'''
# Fill rows starting from index 6 with random SNR values
for index in range(num_rows_to_process, len(input_data)):
    mapped_row = np.zeros(80)
    for i, val in enumerate(input_data.iloc[index]):
        if val == 1:
            mapped_row[i] = np.random.uniform(21.4, 22.5)
        # For 0s, we already have zeros in mapped_row
    
    mapped_snr_data.append(mapped_row)
'''
# Convert the list to a DataFrame
mapped_snr_df = pd.DataFrame(mapped_snr_data)

# Save the DataFrame to a CSV file
mapped_snr_df.to_csv(output_file, index=False, header=False)

print(f'Mapped SNR data has been saved to {output_file}')

