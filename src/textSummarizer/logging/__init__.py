# logging.py in textSummarizer package

import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("textSummarizer")


