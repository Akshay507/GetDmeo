import inspect
import logging

def test_loggingDemo():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler("loging.lg")
    formatter = logging.Formatter("%(asctime)s :%('levelname')s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    return logger