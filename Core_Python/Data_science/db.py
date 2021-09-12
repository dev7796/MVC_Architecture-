# pip install pymysql

import pymysql


def insertLogin():
    connection = pymysql.connect(
        user='root',
        password='gladiators',
        db='PythonFlask'
    )

    id = "1"

    cursor1 = connection.cursor()

    #cursor1.execute("DELETE FROM Flask1")
    cursor1.execute(
        "INSERT INTO Flask1(register id) VALUES ('" + id + "')")

    #stmt = "INSERT INTO loginmaster(loginUsername,loginPassword,loginRole,loginStatus) VALUES ("{}".for)"
    #cursor1.execute(stmt)

    connection.commit()


    cursor1.close()

    connection.close()

insertLogin()
