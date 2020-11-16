from pythonbot.python.config.DataBaseConfig import DataBaseConfig
from pythonbot.python.plugins.contents import PERSONID
from pythonbot.python.utils.OfficialDataUtils import getPlayerName


def insert(sql,values):
    # DataBaseConfig.server.start()
    DataBaseConfig.myConfig.connect()
    cursor = DataBaseConfig.myConfig.cursor()
    try:
        cursor.executemany(sql, values)
        DataBaseConfig.myConfig.commit()
        return 1
    except Exception as e:
        print(e)
        DataBaseConfig.myConfig.rollback()
        return -1
    finally:
        cursor.close()
        DataBaseConfig.myConfig.close()


def select(sql):
    cursor = DataBaseConfig.myConfig.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


if __name__ == '__main__':
    for playerId in PERSONID:
        a = select(
            "SELECT sum(deaths) FROM `dota_match_list` where playerId=%d and start_time between '%s' and '%s'" % (
            playerId, '2019-01-01 00:00:00', '2019-12-31 23:59:59'))
        if (a[0][0] != None):
            print(getPlayerName(playerId) + " 2019年一共被对手免费送回泉水:%d次   共节约TP金额:%d  相当于购买%.2f把圣剑 " % (
            a[0][0], a[0][0] * 50, a[0][0] * 50 / 6200))
