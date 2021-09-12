from wtforms import *


class CategoryVO:
    category_id=IntegerField()
    category_name=StringField()
    category_description=StringField()