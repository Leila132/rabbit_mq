import random
import datetime


class Logger_generator:
    def __init__(self):
        self.level = None
        self.message = None
        self.time = None

    def generate_log(self):
        level = random.randint(1, 3)
        if level == 1:
            self.level = "ERROR"
            self.message = "Database connection failed"
            self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if level == 2:
            self.level = "WARNING"
            self.message = "Uncorrect note"
            self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if level == 3:
            self.level = "INFO"
            self.message = "Note created"
            self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return self.__dict__
