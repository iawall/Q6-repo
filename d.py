import logging
#import loguru
from abc import ABC, abstractmethod

class LogInterface(ABC):
    @abstractmethod
    def debug(self, message):
        print(message)

    @abstractmethod
    def info(self, message):
        print(message)

    @abstractmethod
    def warning(self, message):
        print(message)

    @abstractmethod
    def error(self, message):
        print(message)

    @abstractmethod
    def exception(self, message):
        print(message)

import logging
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        print(message)

    @abstractmethod
    def info(self, message):
        print(message)

    @abstractmethod
    def warning(self, message):
        print(message)

    @abstractmethod
    def error(self, message):
        print(message)

    @abstractmethod
    def exception(self, message):
        print(message)

class LoggingLibrary(Logger):
    def debug(self, message):
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def exception(self, message):
        logging.exception(message)

class Application:
    def __init__(self, logger):
        self.logger = logger

    def main(self):
        self.logger.debug("Debug message")
        self.logger.info("Info message")
        self.logger.warning("Warning message")
        self.logger.error("Error message")
        try:
            1 / 1
        except ZeroDivisionError:
            self.logger.exception("Exception occurred")

def main():
    logging.basicConfig(level=logging.DEBUG)  
    logger = LoggingLibrary()
    app = Application(logger)
    app.main()

if __name__ == "__main__":
    main()
