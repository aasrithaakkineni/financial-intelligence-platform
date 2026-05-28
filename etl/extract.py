import os
import re

print("ETL Extract Process Started")

# SQL file path
sql_file_path = "data/raw/scriptticker.sql"

# Check file exists
if os.path.exists(sql_file_path):

    print("SQL file found successfully!")

    # Read SQL file
    with open(sql_file_path, "r") as file:
        sql_content = file.read()

    # Find CREATE TABLE names
    tables = re.findall(r'CREATE TABLE\s+(\w+)', sql_content, re.IGNORECASE)

    print("\nTABLES FOUND:\n")

    if tables:
        for table in tables:
            print(table)
    else:
        print("No tables found.")

    # Find INSERT statements
    inserts = re.findall(r'INSERT INTO\s+(\w+)', sql_content, re.IGNORECASE)

    print("\nINSERT STATEMENTS FOUND:\n")

    if inserts:
        for insert in inserts:
            print(insert)
    else:
        print("No INSERT statements found.")

else:
    print("SQL file not found.")