# Financial Intelligence Platform

## Overview
This project is a simple ETL pipeline built using Python.

It reads SQL data from a `.sql` file, extracts records using Regex, converts them into a Pandas DataFrame, and exports the cleaned data into CSV format.

---

## Technologies Used
- Python
- Pandas
- Regex
- Git & GitHub

---

## Features
- Reads SQL script file
- Extracts INSERT records
- Converts data into structured table
- Saves output as CSV file

---

## Project Structure

financial-intelligence-platform/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── etl/
│   └── extract.py
│
└── README.md

---

## Output
The extracted data is saved in:

data/cleaned/output.csv

---

## Author
Aasritha
