# coding=utf-8


import pymysql
from sshtunnel import SSHTunnelForwarder


# class DataBaseConfig(object):

# # 郭神mysql
# MYSQL_HOST = "47.101.158.146"
# MYSQL_USERNAME = "root"
# MYSQL_PASSWORD = "942456495"
# MYSQL_DATABASE = "dotaData"
# MYSQL_CHARSET = "utf8"
# db_mysql = pymysql.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE,
#                            charset=MYSQL_CHARSET)
# db_mysql.ping(reconnect=True)
# # 使用cursor()方法获取操作游标
# cursor = db_mysql.cursor()


# class DeveloppmentConfig(DataBaseConfig):
#     DEBUG = True


# config_dict = {
#     'develop': DeveloppmentConfig,
#     'product': ProductionConfig
#
# }


# def connect_mysql():
#     # 打开数据库连接
#     db_mysql = pymysql.connect(DataBaseConfig.MYSQL_HOST, DataBaseConfig.MYSQL_USERNAME, DataBaseConfig.MYSQL_PASSWORD,
#                                DataBaseConfig.MYSQL_DATABASE, charset=DataBaseConfig.MYSQL_CHARSET)
#     db_mysql.ping(reconnect=True)
#     # 使用cursor()方法获取操作游标
#     cursor = db_mysql.cursor()
#     return cursor

def sshConn():
    # 郭神mysql
    MYSQL_HOST = "47.101.158.146"
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "942456495"
    MYSQL_DATABASE = "dotaData"
    MYSQL_CHARSET = "utf8"
    # 配置ssh通道
    server = SSHTunnelForwarder(
        ssh_address_or_host=(MYSQL_HOST, 22),  # 指定ssh登录的跳转机的address
        ssh_username='root',  # 跳转机的用户
        ssh_password='Zx19980601',  # 跳转机的密码
        remote_bind_address=('127.0.0.1', 3306)
    )
    server.start()
    myConfig = pymysql.connect(
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWORD,
        host="127.0.0.1",  # 此处必须是 127.0.0.1
        db=MYSQL_DATABASE,
        port=server.local_bind_port)
    cursor = myConfig.cursor()
    return {'cursor': cursor, 'server': server}


if __name__ == '__main__':
    cursor = sshConn().get('cursor')
    server = sshConn().get('server')
    cursor.execute('SELECT COUNT(*) FROM test;')
    print(cursor.fetchall())
    cursor.close()
    server.close()
