import logging

class Loggen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\nadim\\OneDrive\\Desktop\\nop\\Logs\\automation.log", force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
