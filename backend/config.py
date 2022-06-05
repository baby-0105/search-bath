import os


class DBConfig:
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
