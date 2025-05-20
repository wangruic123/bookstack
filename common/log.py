import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler


class LogHandler:
    def __init__(self):
        self.log_path = Path(__file__).parent.parent / 'log' / 'autotest.log'

    def create_logger(self):
        logger = logging.getLogger("AutoTest")
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 按天轮转日志
        file_handler = TimedRotatingFileHandler(
            filename=self.log_path,
            when='D',
            interval=1,
            backupCount=7
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger


logger = LogHandler().create_logger()