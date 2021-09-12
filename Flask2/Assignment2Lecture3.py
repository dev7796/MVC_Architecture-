from flask import *

app = Flask(__name__)


@app.route('/')
#def load():
#    return render_template('Basic.html')


@app.route('/submit' , methods=['POST', 'GET'])
def submit():

    if request.method=='POST':
        fn1 = request.form.get('Un')
        ln1 = request.form.get('Pass')
        fn = "Python"
        ln = "Flask"
        ls,ls1 = [],[]
        ls.append(fn)
        ls.append(ln)
        ls1.append(fn1)
        ls1.append(ln1)
        print(ls1)
        if fn1==fn and ln1==ln:

            return render_template('Welcome.html', ls=ls)

        else:

            return render_template('Register.html',ls=ls,ls1=ls1)


app.run(threaded=True, port=5678, debug=True)