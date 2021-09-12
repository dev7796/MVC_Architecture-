# pip install pymysql

import pymysql

from flask import *
#from example import *
app = Flask(__name__)
app.secret_key = 'DevShah'
connection = pymysql.connect(
            user='root',
            password='gladiators',
            db='PythonFlask'
        )
cursor1 = connection.cursor()

@app.route('/')
def fn1():
    return render_template('Register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/setsession',methods=['GET','POST'])
def setsession():
    if request.method == "POST":
        user1 = request.form.get('un')
        pass1 = request.form.get('pw')
        fname1 = request.form.get('fn')
        lname1 = request.form.get('ln')
        gender = request.form['gender']
        hobbies = request.form.getlist('Hobby1')
        country = request.form.get('country')
        cursor1.execute(
            "INSERT INTO Flask1(Username , Password, Firstname, Lastname, Hobbies, Gender, Country) VALUES ('" + user1 + "','" + pass1 + "','" + fname1 + "','" + lname1 + "','" + ', '.join(hobbies) + "','" + gender + "','" + country + "')")

        # stmt = "INSERT INTO loginmaster(loginUsername,loginPassword,loginRole,loginStatus) VALUES ("{}".for)"
        # cursor1.execute(stmt)
        session['k1'] = user1
        session['k2'] = pass1
        session['k3'] = fname1
        session['k4'] = lname1
        connection.commit()
        cursor1.close()
        connection.close()
        return render_template('login.html')

@app.route('/getsessionOne',methods=['GET','POST'])
def fn3():
    if request.method == 'POST':
        user2 = request.form.get('un1')
        pass2 = request.form.get('pw1')
        un = session['k1']
        pw = session['k2']
        if user2 != 'admin' or pass2 != 'secret':
            error = 'Invalid credentials'
        if user2 == un and pass2 == pw:
            return render_template('read session2.html')
        else:
            flash('Wrong username or password')
            return redirect(url_for('login'))


# @app.route('/getsessionTwo')
# def fn4():
#     if 'k1' in session:
#         print("hi")
#     else:
#         print("bye")
#
#     return render_template('loginforsession.html')


app.run(threaded=True, port=9000, debug=True)