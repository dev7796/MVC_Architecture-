from flask import request, render_template, redirect, url_for

from Flask9 import app
from Flask9.com.controller.



connection = con_db()

class CategoryDAO:

    def insert_category(self, category_vo):

        cursor1 = connection.cursor()

        cursor1.execute(INSERT INTO categorymaster(categoryName, CategoryDescription) VALUES ('"+ category_vo.category +'))
































