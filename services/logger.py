import os
import logging
from configs import configs


LOGGING_DIR = os.path.dirname(__file__)+"/../logs"


class Logger(object):
    def __init__(self, name):
        name = name.replace('.log', '')
        logger = logging.getLogger('log_namespace.%s' % name)
        stream_level = getattr(logging, configs.LOGGER_LEVEL)
        logger.setLevel(stream_level)
        if not logger.handlers:
            if not os.path.exists(LOGGING_DIR):
                os.mkdir(LOGGING_DIR)
            file_name = os.path.join(LOGGING_DIR, 'genesis.log')
            formatter = logging.Formatter('[%(asctime)s %(levelname)s:%(name)s - %(funcName)s() line %(lineno)d] - %(message)s')

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            info_file_handler = logging.FileHandler(file_name)
            info_file_handler.setFormatter(formatter)
            info_file_handler.setLevel(logging.DEBUG)

            logger.addHandler(stream_handler)
            if configs.LOG_TO_FILE:
                logger.addHandler(info_file_handler)
        self._logger = logger

    def get(self):
        return self._logger
