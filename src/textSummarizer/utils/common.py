import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any
import logging



logging.info("Successfully loaded YAML file")


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"Successfully loaded YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")

   

def create_directories(path_to_directories : list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
            


def get_size(path: Path) -> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"