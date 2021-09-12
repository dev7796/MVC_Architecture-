from wtforms import *


class SubcategoryVO:
    subcategory_id = IntegerField()
    subcategory_name = StringField()
    subcategory_description = StringField()
    subcategory_category_id = IntegerField()

