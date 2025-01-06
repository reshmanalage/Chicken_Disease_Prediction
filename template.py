import os
import logging
from pathlib import Path

# Set up logging with level DEBUG to log detailed information
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")

project_name = "cnnClassifier"  # Name of the project

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Iterate over each file in the list
for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    logging.debug(f"Processing: {filepath}")
    
    # Split the path into directory and filename
    filedir, filename = os.path.split(filepath)
    logging.debug(f"Directory: {filedir}, Filename: {filename}")
    
    # Create directory if necessary
    if filedir:  # Checks if the directory part is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    
    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w"):
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists and is not empty")
