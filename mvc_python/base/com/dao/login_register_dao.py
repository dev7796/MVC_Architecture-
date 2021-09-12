from base.com.dao import *


class CategoryDAO:
    def register_user(self,category_vo):
        connection = connection_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO login_register_table( firstname , lastname , username , password) VALUES ('" + category_vo.firstname + "','" + category_vo.lastname + "','" + category_vo.username + "','" + category_vo.password + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def login_user(self, category_vo):
        connection = connection_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM login_register_table WHERE username = '"+ category_vo.username + "'")
        user_data = cursor.fetchall()
        print(user_data)
        connection.commit()
        cursor.close()
        connection.close()
        return user_data