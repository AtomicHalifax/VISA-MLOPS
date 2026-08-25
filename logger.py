import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory path (e.g., 'logs' folder inside current directory)
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path for the current log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH), # Writes to file
        logging.StreamHandler()             # Prints to console
    ]
)

# Test script execution
if __name__ == "__main__":
    logging.info("Testing MLOps Logger: Logging system initiated successfully.")
    logging.warning("Testing MLOps Logger: This is a warning test message.")
    logging.error("Testing MLOps Logger: This is an error test message.")