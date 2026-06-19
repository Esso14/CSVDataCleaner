import json
import os
from pathlib import Path
import logging
from logging.config import fileConfig

os.chdir(Path(__file__).parent)

#Load configuration
fileConfig("config/logging.ini")

logger = logging.getLogger()  # from root

logger.info("CSV-DataCleaner configuration is started ...")

with open("config/config.json", mode="r", encoding="utf-8") as file:
    config_file = json.load(file)
    logger.info("Configuration file is loaded")

INPUT_FILE = config_file["input_file"]
CLEANED_FILE = config_file["cleaned_file"]

REPORT_INPUT_FILE = config_file["report_input_file"]
REPORT_CLEANED_FILE = config_file["report_cleaned_file"]


logger.info("Application CSV-DataCleaner config is closed!")