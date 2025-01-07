import os
import sys
import logging

# Set the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the log directory and log file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the defined logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Log to the console (stdout)
    ]
)

# Get the logger
logger = logging.getLogger("cnnClassifierLogger")

# Example code to log messages
def process_data():
    try:
        # Log info message when starting a task
        logger.info("Started processing data")

        # Simulate data processing
        # (Insert your data processing logic here)
        
        # Log warning if there is a minor issue (example)
        logger.warning("Warning: Data processing is taking longer than expected")

        # Simulate successful completion of data processing
        logger.info("Data processing completed successfully")

    except Exception as e:
        # Log an error if something goes wrong
        logger.error(f"Error occurred during data processing: {e}")

# Example function call
process_data()
