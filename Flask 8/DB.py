# pip install pymysql

import pymysql
from flask import *

app = Flask(__name__)
app.secret_key = 'DevShah'
connection = pymysql.connect(
            user='root',
            password='gladiators',
            db='PythonFlask',
            cursorclass=pymysql.cursors.DictCursor
            )
cursor1 = connection.cursor()

@app.route('/')
def fn1():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('Register.html')

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
        connection.commit()
        return render_template('login.html')

@app.route('/getsessionOne',methods=['GET','POST'])
def fn3():
    ls=[]
    un_ls=[]
    pw_ls=[]
    fn_ls=[]
    ln_ls=[]
    if request.method == 'POST':
        user2 = request.form.get('un1')
        pass2 = request.form.get('pw1')
        cursor1.execute("SELECT Username,Password,Firstname,Lastname FROM Flask1")
        unAndpw_list=cursor1.fetchall()
        for dictionary in unAndpw_list:
             for key in dictionary.keys():
                 if key=='Username':
                     un_ls.append(dictionary[key])
                 elif key == 'Password':
                     pw_ls.append(dictionary[key])
                 elif key == 'Firstname':
                     fn_ls.append(dictionary[key])
                 elif key == 'Lastname':
                     ln_ls.append(dictionary[key])

        if user2 in un_ls and pass2 in pw_ls :
            un_index =  un_ls.index(user2)
            ls.append(fn_ls[un_index])
            ls.append(ln_ls[un_index])
            return render_template('read session2.html',ls=ls)
        elif user2 not in un_ls and pass2 in pw_ls:
            flash('Wrong username','error')
            return redirect(url_for('fn1'))
        elif user2 in un_ls and pass2 not in pw_ls:
            flash('Wrong Password','error1')
            return redirect(url_for('fn1'))
        else:
            flash('Wrong Username and Password','error2')
            return redirect(url_for('fn1'))

app.run(threaded=True, port=9000, debug=True)