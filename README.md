# Financial Intelligence Platform

## Overview

This project is a simple ETL (Extract, Transform, Load) pipeline built using Python.

The project reads data from a SQL file, extracts records, cleans the data, and exports the processed data into CSV format.

---

## Technologies Used

- Python
- Pandas
- SQL
- HTML
- CSS
- JavaScript
- GitHub

---

## Project Structure

```
financial-intelligence-platform/

├── data/
│   ├── raw/
│   │   └── scriptticker.sql
│   └── cleaned/
│       ├── output.csv
│       └── cleaned_output.csv

├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── test.py

├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js

├── README.md
└── requirements.txt
```

---

## Modules

### Extract Module

- Reads records from SQL file.
- Extracts required data.
- Converts extracted data into CSV format.

### Transform Module

- Removes duplicate records.
- Handles missing values.
- Cleans text fields.
- Generates cleaned CSV output.

---

## Frontend

Frontend runs on:

```
http://localhost:8000
```

### Frontend Features

- Displays processed stock data.
- Interactive button using JavaScript.
- Tabular data representation.
- Simple and responsive user interface.

---

## Backend

Backend consists of ETL modules written in Python.

### Extract Process

- Reads SQL file from data/raw folder.
- Extracts stock information.
- Generates output.csv.

### Transform Process

- Reads extracted CSV.
- Removes duplicate values.
- Removes null values.
- Cleans text data.
- Generates cleaned_output.csv.

---

## Output Files

The processed files are stored in:

```
data/cleaned/output.csv
data/cleaned/cleaned_output.csv
```

---

## Features

- ETL Pipeline Implementation
- Data Cleaning and Transformation
- CSV Generation
- Frontend Data Display
- GitHub Version Control
- Documentation Support

---

## Future Improvements

- Database Integration
- Real-Time Data Processing
- Dashboard Visualization
- Automated ETL Scheduling
- API Integration

---

## Author

Aasritha Akkineni