from flask import *

app = Flask(__name__)


@app.route('/')
def load():
    return render_template('HelloWorld.html')


@app.route('/submit')
def submit():
    return "<h1>Its Render_Template Example</h1>"


app.run(debug=True)
