# coding=utf-8

import pymysql
from sshtunnel import SSHTunnelForwarder


class DataBaseConfig(object):
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
    myConfig.ping(reconnect=True)

    cursor = myConfig.cursor()


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

    return {'cursor': cursor, 'server': server,'conn':myConfig}


if __name__ == '__main__':
    cursor = DataBaseConfig.myConfig.cursor()
    cursor.execute(
        'INSERT INTO `dotaData`.`dota_match_list`(`match_id`, `player_slot`, `radiant_win`, `game_mode`, `duration`, `lobby_type`, `hero_id`, `start_time`, `version`, `kills`, `deaths`, `assists`, `skill`, `leaver_status`, `party_size`, `playerId`) VALUES (5664603222, 4, 1, 3, 2683, 0, 94, 1603195665000, null, 4, 4, 9, null, 0, 4, 442726378);')
    DataBaseConfig.myConfig.commit()
    cursor.close()
    DataBaseConfig.myConfig.close()
    DataBaseConfig.server.close()
