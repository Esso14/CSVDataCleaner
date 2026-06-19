import pandas as pd
import os
import logging
from ydata_profiling import ProfileReport

logger = logging.getLogger()

class CleanerCSV:

    def __init__(self, file_path: str, sep: str = ',', encoding: str = 'utf-8'):
        # Class initialisation and load csv-date into Pandas DataFrame
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File in {file_path} not found.")
        
        self.file_path = file_path
        self.sep = sep
        self.encoding = encoding
        # Load the data into a copie and preserve the original state
        self.df = pd.read_csv(file_path, sep=sep, encoding=encoding)
        logger.info(f"Data set successfully loaded. Form: {self.df.shape[0]} rows, {self.df.shape[1]} columns.")

    
    
    def generate_profile(self, output_html: str = "preprocess/daten_profiling_report.html", title: str = "Standard Profiling Report"):
        """
        Creates a comprehensive EDA (Exploratory Data Analysis)-report using ydata_profiling and saves it as HTML.
        """
        logger.info(f" Generate Profiling-report: '{title}'...")
        # Generate the report directly from the integrated DataFrame
        profile = ProfileReport(self.df, title=title, explorative=True)
        profile.to_file(output_html)
        logger.info(f"Report successfully saved as '{output_html}'.")
    

    def clean_whitespaces(self) -> 'CleanerCSV':
        """
        Removes leading and trailing spaces from all string columns (stripping)).
        """
        # In Python (pandas), text columns (strings) are typically stored as "object" by default
        string_cols = self.df.select_dtypes(include=['object']).columns
        for col in string_cols:
            self.df[col] = self.df[col].astype(str).str.strip()
        logger.info(" Unwanted Whitespaces have been removed.")
        return self

    
    def remove_duplicates(self) -> 'CleanerCSV':
        """
        Identify and remove completely identical data rows.
        """
        initial_rows = len(self.df)
        self.df.drop_duplicates(inplace=True)
        current_rows = len(self.df)
        print(f" Duplicates removed: {initial_rows - current_rows} rows deleted.")
        return self

    
    def handle_missing_values(self, strategy: str = 'drop', columns: list = None, fill_value=None) -> 'CleanerCSV':
        """
        Handles missing values (NaN). 
        Strategies: 'drop' (drop rows) or 'fill' (fill with fill_value).
        """
        if strategy == 'drop':
            self.df.dropna(subset=columns, inplace=True)
            logger.info(f" Rows with missing values deleted (column filter: {columns})")
        elif strategy == 'fill':
            if fill_value is None:
                raise ValueError("A 'fill_value' must be provided for the 'fill' strategy..")
            if columns:
                for col in columns:
                    self.df[col].fillna(fill_value, inplace=True)
            else:
                self.df.fillna(fill_value, inplace=True)
            logger.info(f" Missing values filled with '{fill_value}'.")
        else:
            logger.error(" Unknown strategy. No missing values handled.")
        return self

    
    def standardise_dates(self, date_columns: list, date_format: str = None) -> 'CleanerCSV':
        """
        Converts specified columns to a uniform datetime format.
        """
        for col in date_columns:
            self.df[col] = pd.to_datetime(self.df[col], format=date_format, errors='coerce')
        logger.info(f" Standardized date columns: {date_columns}")
        return self

    
    def export_csv(self, output_path: str = "preprocess/clean_data.csv", sep: str = ';', encoding: str = 'utf-8-sig'):
        """
        Exports the cleaned DataFrame to a new CSV file. 
        'utf-8-sig' is recommended so that Excel reads umlauts correctly right away.
        """
        self.df.to_csv(output_path, sep=sep, index=False, encoding=encoding)
        logger.info(f" Cleaned data successfully exported to: {output_path}")

##-------------------------------
# Special for my csv-file
#-------------------------------

    def correct_datatype(self) -> 'CleanerCSV':

        self.df["Order ID"] = pd.to_numeric(self.df["Order ID"], errors="coerce")
        self.df["Quantity Ordered"] = pd.to_numeric(self.df["Quantity Ordered"], errors="coerce")
        self.df["Price Each"] = pd.to_numeric(self.df["Price Each"], errors="coerce")
        self.df["Order Date"] = pd.to_datetime(self.df["Order Date"], errors="coerce")
        return self


    