import os
import re
import pandas as pd

print("ETL Extract Process Started")

# SQL file path
sql_file_path = "data/raw/scriptticker.sql"

# Check if file exists
if os.path.exists(sql_file_path):

    print("SQL file found successfully!")

    # Read SQL file
    with open(sql_file_path, "r") as file:
        sql_content = file.read()

    # Extract table names
    tables = re.findall(r'CREATE TABLE\s+(\w+)', sql_content, re.IGNORECASE)

    print("\nTABLES FOUND:")
    print(tables)

    # Extract INSERT values
    values = re.findall(r'\((\d+),\s*\'([^\']+)\'\)', sql_content)

    print("\nEXTRACTED RECORDS:")
    print(values)

    # Convert to DataFrame
    df = pd.DataFrame(values, columns=["id", "name"])

    print("\nDATAFRAME:")
    print(df)

    # Save CSV
    output_path = "data/cleaned/output.csv"

    df.to_csv(output_path, index=False)

    print(f"\nCSV file saved at: {output_path}")

else:
    print("SQL file not found.")