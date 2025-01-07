import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger  # Custom logger from cnnClassifier module
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import logging

# Set up logging configuration (this is the logging setup)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler('app.log'), logging.StreamHandler()]
)

# Ensure logger is initialized and configured
logger = logging.getLogger("cnnClassifier")

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        logger.error(f"An error occurred while reading the YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Creates the directory if it doesn't exist
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save JSON file at {path}: {e}")
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path, "r") as f:
            content = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Failed to decode JSON from: {path}")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the JSON file from {path}: {e}")
        raise

@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save binary file at {path}: {e}")
        raise

@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.error(f"Failed to load binary file from {path}: {e}")
        raise

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

def decode_image(imgstring: str, file_name: str):
    imgdata = base64.b64decode(imgstring)
    with open(file_name, 'wb') as f:
        f.write(imgdata)

def encode_image_into_base64(cropped_image_path: str) -> str:
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
