import logging 
import os
from datetime import datetime

LOG_FILE_PATH = os.path.join(os.getcwd(), 'networksecurity', 'logging', 'logs', f'log_{datetime.now().strftime("%Y-%m-%d")}.log')

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

