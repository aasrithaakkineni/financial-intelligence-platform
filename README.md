# Financial Intelligence Platform

## Overview
This project is a simple ETL (Extract, Transform, Load) pipeline built using Python.

The project reads data from a SQL file, extracts records, cleans the data, and exports the processed data into CSV format.

## Technologies Used
- Python
- Pandas
- SQL
- GitHub

## Project Structure

financial-intelligence-platform/
│
├── data/
│ ├── raw/
│ │ └── scriptticker.sql
│ └── cleaned/
│ ├── output.csv
│ └── cleaned_output.csv
│
├── etl/
│ ├── extract.py
│ └── transform.py
│
├── README.md
└── requirements.txt

## Modules

### Extract Module
- Reads data from SQL file.
- Extracts records using Python.

### Transform Module
- Removes duplicate records.
- Handles missing values.
- Cleans text fields.
- Generates cleaned CSV output.

## Output
The cleaned data is stored in:

data/cleaned/cleaned_output.csv

## Future Improvements
- Database integration
- Automated ETL scheduling
- Dashboard visualization
- Advanced data validation

## Author
Aasritha Akkineni