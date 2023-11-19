import pandas as pd

# Define the path to the Excel file
excel_file_path = 'C:\\Users\\tange\\BERTFED\\docs\\business_understanding\\Data LSTM and Pronostic.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(excel_file_path)

# Create a dictionary to hold the DataFrames
dataframes_dict = {}

# Iterate through each sheet name and read the sheet into a DataFrame
for sheet_name in xlsx.sheet_names:
    dataframes_dict[sheet_name] = pd.read_excel(xlsx, sheet_name)

# Now dataframes_dict contains all  data, accessible by sheet name
# This will print out all the keys (sheet names) in the dataframes_dict
for key in dataframes_dict.keys():
    print(key)
