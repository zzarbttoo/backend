import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import os 

def configure_logger(log_directory= 'monitor'):

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 콘솔 핸들러 추가
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    current_date = datetime.now().strftime('%Y-%m-%d')

    file_handler = TimedRotatingFileHandler(
        filename=f'{log_directory}/pulse_log_file_{current_date}.log',
        when='D', # Daily rotation
        interval=1, # One day
        backupCount=7, # Keep one week of log files
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)

    # 로그 포매터 추가
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 핸들러를 로거에 추가
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)  # 이 부분을 추가합니다.

    return logger

