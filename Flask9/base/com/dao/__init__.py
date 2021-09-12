import pymysql


def con_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
