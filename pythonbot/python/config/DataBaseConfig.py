# coding=utf-8


import pymysql


class DataBaseConfig(object):
    # 配置mysql信息

    MYSQL_HOST = ""
    MYSQL_USERNAME = ""
    MYSQL_PASSWORD = ""
    MYSQL_DATABASE = "dotaData"
    MYSQL_CHARSET = "utf8"

    db_mysql = pymysql.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE,
                               charset=MYSQL_CHARSET)
    db_mysql.ping(reconnect=True)
    # 使用cursor()方法获取操作游标
    cursor = db_mysql.cursor()


class DeveloppmentConfig(DataBaseConfig):
    DEBUG = True


class ProductionConfig(DataBaseConfig):
    pass


config_dict = {
    'develop': DeveloppmentConfig,
    'product': ProductionConfig

}


def connect_mysql():
    # 打开数据库连接
    db_mysql = pymysql.connect(DataBaseConfig.MYSQL_HOST, DataBaseConfig.MYSQL_USERNAME, DataBaseConfig.MYSQL_PASSWORD,
                               DataBaseConfig.MYSQL_DATABASE, charset=DataBaseConfig.MYSQL_CHARSET)
    db_mysql.ping(reconnect=True)
    # 使用cursor()方法获取操作游标
    cursor = db_mysql.cursor()
    return cursor
