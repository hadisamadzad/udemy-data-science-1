class Log:
    def __init__(self, level, text):
        self.level = level
        self.text = text

    def log_on_console(self):
        if (self.level is ""):
            raise RuntimeError("Invalid log level")
        print(f'{self.level}: {self.text}')