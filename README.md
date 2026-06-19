# CSV Data Cleaner

The primary goal of this project is to create a robust and versatile class named CleanerCSV. This class should be able of processing CSV datasets while incorporating several common data cleaning tasks.


---
## Features:

- creates a copy of the original CSV-file
- Performs data cleaning tasks on the copy like:
  - removing duplicates
  - cleansing erroneous values
  - convert to the correct data types
  - fillna
  - etc.
- generates profiles with `ydata_profiling` for both CSV-files --> the original csv-file and cleaned csv-file


---
## Project Structure

<pre>
    CSVDataCleaner/
    │
    ├── config/
    │   └── config.json
    │   └── logging.ini
    │
    ├── data/
    │   └── your_raw_data.csv
    │   └── cleaned_data.csv
    │   └── report_before_cleaning.html
    │   └── report_after_cleaning.html
    │        
    │
    ├── logs/
    │   └── app.log
    │
    ├── app.py
    ├── config.py
    ├── cleanercsv.py
    ├── README.md
    └── requirements.txt
</pre>


---
## Installation  & Setup

To use this app, you have to ensure you have installed Python.
You need also a Browser to read the Profile-file that will be generated.

### 1. Clone the repository

`git clone <https://github.com/Esso14/CSVDataCleaner`


### 2. Load your_raw_data.csv in order data

Open config.json and fixe your csv-file:

        ```JSON
        {
            "input_file": "data/your_raw_data.csv",
            ...
        }
        ```

### 3. Quick Start

Start the application with: `python3 app.py`

---
## Technologie used

- Python 3.x
  
## License

This project is free to use and can be extended as needed
