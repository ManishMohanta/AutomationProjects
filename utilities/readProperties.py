import configparser

config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password

    @staticmethod
    def getURL():
        url = config.get('common info1', 'baseURL')
        return url