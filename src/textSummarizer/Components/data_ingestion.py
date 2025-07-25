import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from shutil import copyfileobj
from textSummarizer.entity import DataIngestionConfig
import shutil

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                print(f"📥 Downloading from: {self.config.source_url}")
                with urllib.request.urlopen(self.config.source_url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to download. Status code: {response.status}")
                    
                    with open(self.config.local_data_file, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                logger.info(f" File downloaded to {self.config.local_data_file}")
            except Exception as e:
                logger.error(f" Download failed: {e}")
                raise e
        else:
            logger.info(f"File already exists: {get_size(Path(self.config.local_data_file))}")

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)