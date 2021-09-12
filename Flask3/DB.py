# pip install pymysql

import pymysql


def insertLogin():
    connection = pymysql.connect(
        user='root',
        password='gladiators',
        db='PythonFlask'
    )

    un = "admin"
    pwd = "admin"
    #role = "admin"
    #status = "active"

    cursor1 = connection.cursor()

    cursor1.execute(
        "INSERT INTO Flask1(Username , Password) VALUES ('" + un + "','" + pwd + "')")

    #stmt = "INSERT INTO loginmaster(loginUsername,loginPassword,loginRole,loginStatus) VALUES ("{}".for)"
    #cursor1.execute(stmt)

    connection.commit()


    cursor1.close()

    connection.close()

insertLogin()
