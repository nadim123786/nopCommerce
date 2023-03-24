import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\nadim\\OneDrive\\Desktop\\nop\\Configuration\\config.ini")

class ReadData:
    @staticmethod
    def read_baseURL():
        return config.get('common info', 'baseURL')
    
    @staticmethod
    def read_email():
        return config.get('common info', 'email')
    
    @staticmethod
    def read_password():
        return config.get('common info', 'password')
    