from flask import *
from Flask_Assignment_3 import *


app = Flask(__name__)


def fn5():
    if 'k1' in session:
        a = session.get('k1')
        print(a)

# @app.route('/visits')
# def visits():
#     if 'k1' in session:
#         a = session.get('k1')  # reading and updating session data
#         print(a)
#     else:
#         session['visits'] = 1 # setting session data
#     return "Total visits: {}".format(session.get('visits'))
#
#
# app.run(threaded=True, port=5679, debug=True)
