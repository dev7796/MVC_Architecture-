from base import *

class CategoryDAO:
    def insert_category(self,category_vo):
        db.session.add(category_vo)
        db.session.commit()

