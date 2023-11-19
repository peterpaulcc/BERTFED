import pandas as pd

# Define the path to the Excel file
excel_file_path = r'C:\Users\tange\BERTFED\docs\business_understanding\Data LSTM and Pronostic.xlsx'

# Load the Excel file
xlsx = pd.ExcelFile(excel_file_path)

# Save each sheet as a CSV file
for sheet_name in xlsx.sheet_names:
    df = pd.read_excel(xlsx, sheet_name)
    csv_file_path = f'{sheet_name}.csv'  # This will create a CSV file named after the sheet
    df.to_csv(csv_file_path, index=False)  # Save DataFrame to CSV without the index


