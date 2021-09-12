from wtforms import *


class CategoryVO:
    login_id = IntegerField()
    firstname = StringField()
    lastname = StringField()
    username = StringField()
    password = StringField()
