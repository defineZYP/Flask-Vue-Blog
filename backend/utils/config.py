'''
configs of Flask app
'''
import os


class Config:
    '''
    something that define the flask app
    '''
    def __init__(self):
        self.DEBUG = True
        self.LOG_LEVEL = "INFO"
        self.DIALECT = "mysql"
        self.DRIVER = "pymysql"
        self.USERNAME = "claude"
        self.PASSWORD = "tifatifasql123"
        self.HOST = "localhost"
        self.PORT = "3306"
        self.DATABASE = "TaleGarden"
        self.SECRET_KEY = "the random string"
        self.SQLALCHEMY_DATABASE_URI = f"{self.DIALECT}+{self.DRIVER}://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False