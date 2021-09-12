import pymysql


def connection_db():
    connection = pymysql.connect(
        user='root',
        password='gladiators',
        db='PythonFlask',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection