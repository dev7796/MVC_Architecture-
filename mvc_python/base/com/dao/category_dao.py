from base.com.dao import *


class CategoryDAO:
    def insert_category(self,category_vo):
        connection = connection_db()
        cursor=connection.cursor()

        cursor.execute("insert into category_table(categoryName,categoryDescription) VALUES ('"+category_vo.category_name+"','"+category_vo.category_description+"')")

        connection.commit()
        cursor.close()
        connection.close()

    def view_category(self):
        print("In View_Category")
        connection = connection_db()
        cursor = connection.cursor()
        sql="SELECT * FROM category_table"
        cursor.execute(sql)
        data0 = cursor.fetchall()
        print(data0)
        cursor.close()
        connection.close()
        return data0

    def delete_category(self, category_vo):
        id = category_vo.category_id
        connection = connection_db()
        cursor = connection.cursor()
        cursor.execute("DELETE from category_table WHERE categoryID =" + id)
        connection.commit()
        cursor.close()
        connection.close()


    def edit_category(self, category_vo):
        id = category_vo.category_id
        connection = connection_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM category_table WHERE categoryID =" + id)
        edited_data = cursor.fetchall()
        print("this is edit", edited_data)
        cursor.close()
        connection.close()
        return edited_data


    def update_category(self, category_vo):
        id = category_vo.category_id
        name = category_vo.category_name
        description = category_vo.category_description
        print(id, name,description)
        connection = connection_db()
        cursor = connection.cursor()
        sql = (
            "UPDATE category_table SET categoryName=%s, categoryDescription=%s WHERE categoryID=%s")
        val = (name, description, id)
        cursor.execute(sql, val)
        connection.commit()
        connection.close()

    def load_subcategory(self):
        connection = connection_db()
        cursor = connection.cursor()
        sql = "SELECT categoryID,categoryName FROM category_table"
        cursor.execute(sql)
        category_data = cursor.fetchall()
        print(category_data)
        cursor.close()
        connection.close()
        return category_data
