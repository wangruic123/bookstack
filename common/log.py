# common/log.py
import logging
import sys
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler


class LogHandler:
    def __init__(self):
        self.logger = logging.getLogger("AutoTest")
        self.logger.setLevel(logging.DEBUG)
        self._setup_handlers()

    def _setup_handlers(self):
        # 文件处理器
        log_path = Path(__file__).parent.parent / 'log' / 'autotest.log'
        file_handler = TimedRotatingFileHandler(
            filename=log_path,
            when='midnight',
            backupCount=7,
            encoding='utf-8'
        )
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        # 控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


logger = LogHandler().logger