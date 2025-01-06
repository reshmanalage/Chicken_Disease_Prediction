import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/your_project_name/__init__.py",
    f"src/your_project_name/components/__init__.py",
    f"src/your_project_name/utils/__init__.py",
    f"src/your_project_name/config/__init__.py",
    f"src/your_project_name/config/configuration.py",
    f"src/your_project_name/pipeline/__init__.py",
    f"src/your_project_name/entity/__init__.py",
    f"src/your_project_name/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    logging.debug(f"Processing: {filepath}")
    
    # Split into directory and filename
    filedir, filename = os.path.split(filepath)
    logging.debug(f"Directory: {filedir}, Filename: {filename}")
    
    # Create directory if needed
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Create file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
