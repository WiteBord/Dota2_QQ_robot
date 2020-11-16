from pythonbot.python.config.DataBaseConfig import DataBaseConfig


def insert(sql,values):
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
        DataBaseConfig.server.close()
