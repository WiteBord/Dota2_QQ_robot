from pythonbot.python.config import DataBaseConfig


def insert(sql,values):
    cursor = DataBaseConfig.sshConn().get('cursor')
    server = DataBaseConfig.sshConn().get('server')
    conn = DataBaseConfig.sshConn().get('conn')
    cursor.executemany(sql,values)
    conn.commit()
    cursor.close()
    conn.close()
    server.close()