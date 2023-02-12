import logging


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s: %(message)s',
                            handlers=[logging.StreamHandler()])

    def debug(self, message):
        self.logger.debug(message)
