import configparser

config=configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getAppURL():
        url=config.get('Common Info','baseURL')
        return url

    @staticmethod
    def getusername():
        username=config.get('Common Info','username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('Common Info','password')
        return password