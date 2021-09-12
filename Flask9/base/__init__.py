from flask import Flask

app = Flask(__name__)

app.secret_key = 'sessionData'

app.config['TESTING'] = True

print("in mvc_python")

import base.com.controller
