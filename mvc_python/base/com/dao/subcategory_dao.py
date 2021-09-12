from base.com.dao import *


class SubcategoryDAO:

   def insert_subcategory(self,subcategory_vo):
        connection = connection_db()
        cursor = connection.cursor()
        print(subcategory_vo.subcategory_category_id,subcategory_vo.subcategory_description,subcategory_vo.subcategory_name)
        cursor.execute(
         "insert into subcategory_table(subcategory_name, subcategory_category_id, subcategory_description) VALUES ('" + subcategory_vo.subcategory_name + "', '"+ subcategory_vo.subcategory_category_id +"' ,'" + subcategory_vo.subcategory_description + "')")

        connection.commit()
        cursor.close()
        connection.close()

   def view_subcategory(self):
       print("In View_subCategory")
       connection = connection_db()
       cursor = connection.cursor()
       sql = "SELECT subcategory_table.subcategory_id, subcategory_table.subcategory_name, category_table.categoryName, subcategory_table.subcategory_description  FROM category_table  INNER JOIN subcategory_table ON category_table.categoryID=subcategory_table.subcategory_category_id;"
       cursor.execute(sql)
       user_data = cursor.fetchall()
       print(user_data)
       cursor.close()
       connection.close()
       return user_data

   def delete_subcategory(self, subcategory_vo):
       id = subcategory_vo.subcategory_id
       connection = connection_db()
       cursor = connection.cursor()
       cursor.execute("DELETE from subcategory_table WHERE subcategory_id =" + id)
       connection.commit()
       cursor.close()
       connection.close()

   def edit_subcategory(self, subcategory_vo):
       id = subcategory_vo.subcategory_id
       connection = connection_db()
       cursor = connection.cursor()
       cursor.execute("SELECT * FROM subcategory_table WHERE subcategory_id =" + id)
       edited_data = cursor.fetchall()
       print("this is edit", edited_data)
       cursor.close()
       connection.close()
       return edited_data

   def update_subcategory(self, subcategory_vo):
       id = subcategory_vo.subcategory_id
       name = subcategory_vo.subcategory_name
       description = subcategory_vo.subcategory_description
       print(id, name, description)
       connection = connection_db()
       cursor = connection.cursor()
       sql = (
           "UPDATE subcategory_table SET subcategory_name=%s, subcategory_description=%s WHERE subcategory_id=%s")
       val = (name, description, id)
       cursor.execute(sql, val)
       connection.commit()
       connection.close()