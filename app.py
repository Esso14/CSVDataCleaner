from pathlib import Path
import config as cfg
from cleanercsv import CleanerCSV

import os
import logging
from logging.config import fileConfig

os.chdir(Path(__file__).parent)

#Load configuration
fileConfig("config/logging.ini")

logger = logging.getLogger()  # from root


def main():

    logger.info("Welcome to CSV-DataCleaner!")

    # 1. Initialize pipeline (load raw data)
    # File is assumed to exist here
    cleaner = CleanerCSV(file_path=cfg.INPUT_FILE, sep=",", encoding="utf-8")
    
    
    # 2. Perform data profiling BEFORE cleaning
    cleaner.generate_profile(output_html=cfg.REPORT_INPUT_FILE, title="Analysis: Raw data")

    
    # 3. Chaining the cleaning pipeline: Method chaining
    (cleaner.clean_whitespaces()
            .remove_duplicates()
            #.handle_missing_values(strategy='fill', columns=['Status'], fill_value='Unbekannt')
            .correct_datatype()
            )

    # 4. Perform data profiling AFTER cleansing
    cleaner.generate_profile(output_html=cfg.REPORT_CLEANED_FILE, title="Analysis: Cleaned data")


    # 5. Export clean result
    cleaner.export_csv(cfg.CLEANED_FILE, sep=";")


if __name__ == '__main__':
    main()
    