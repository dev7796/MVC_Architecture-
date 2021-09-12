from flask import *

app = Flask(__name__)
app.secret_key = 'Dev'


@app.route('/')
def fn1():
    return render_template('loginforsession.html')


@app.route('/setsession')
def fn2():

    user = request.args.get('un')
    session['k1']=user
    return render_template('read session1.html')


@app.route('/getsessionOne')
def fn3():

    un=session['k1']
    print(un)

    return render_template('read session2.html')


@app.route('/getsessionTwo')
def fn4():

    if 'k1' in session:
        print("hi")
    else:
        print("bye")

    return render_template('loginforsession.html')

app.run(debug=True)
