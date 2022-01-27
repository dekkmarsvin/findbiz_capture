from asyncio.log import logger
import logging
import sys

def getlogger():
    from datetime import datetime

    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger(__name__)
    rootLogger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}/{1}.log".format('log', '{:%Y-%m-%d}.log'.format(datetime.now())))
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    return rootLogger