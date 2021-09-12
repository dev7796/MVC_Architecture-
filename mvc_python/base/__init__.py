from flask import Flask
app=Flask(__name__)

app.secret_key='FlaskProject'

app.config['TESTING'] = True

print('in base')

import base.com.controller