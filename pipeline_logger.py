import logging
import os
from datetime import datetime

def get_logger(name: str) -> logging.Logger:
    os.makedirs('logs', exist_ok=True)

    log_filename = f'logs/pipeline_{datetime.now().strftime('%y%m%d')}.log'

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_filename)
        ]
    )

    return logging.getLogger(name)