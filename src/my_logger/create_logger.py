from datetime import datetime
import os

class Logger:
    DEBUG = "[DEBUG]"
    INFO = "[INFO]"
    WARNING = "[WARNING]"
    ERROR = "[ERROR]"
    FILEPATH = f"{os.getcwd()}".rsplit("src")[0] + "//log//"

    def __init__(self):
        self.__root = None

    def set_log_file(self, root):
        if not os.path.exists(f"{self.FILEPATH + root}.txt"):
            open(f"{self.FILEPATH + root}.txt", "w").close()
        self.__root = root

    def debug(self, mes):
        with open(f"{self.FILEPATH + self.__root}.txt", "a") as f:
            f.write(Logger.DEBUG + " " + str(datetime.now()) + " " + mes + "\n")

    def info(self, mes):
        with open(f"{self.FILEPATH + self.__root}.txt", "a") as f:
            f.write(Logger.INFO + " " + str(datetime.now()) + " " + mes + "\n")

    def warning(self, mes):
        with open(f"{self.FILEPATH + self.__root}.txt", "a") as f:
            f.write(Logger.WARNING + " " + str(datetime.now()) + " " + mes + "\n")

    def error(self, mes):
        with open(f"{self.FILEPATH + self.__root}.txt", "a") as f:
            f.write(Logger.ERROR + " " + str(datetime.now()) + " " + mes + "\n")

logger = Logger()