# convert excel file into csv format

import pandas as pd

# Load the Excel file
excel_file = "data/data.xlsx"  # Replace with your file path
df = pd.read_excel(excel_file)

# Save as CSV
csv_file = "data/output_file.csv"  # Replace with your desired output file name
df.to_csv(csv_file, index=False)

print(f"File saved as {csv_file}")
