import pymysql
import pymysql.cursors
from flask import *

app = Flask(__name__)
app.secret_key = 'DevShah'

def connection():
    connection = pymysql.connect(
        user='root',
        password='Gladiators7',
        db='PythonFlask',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
@app.route('/')
def fn1():
    return render_template('homepage.html')

@app.route("/register")
def register():
    return render_template('Register.html')

@app.route('/login')
def login():
    return render_template('Login.html')



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
        #id1 = request.form.get('id')
        con=connection()
        cursor1=con.cursor()
        cursor1.execute(
            "INSERT INTO Flask2( Username , Password, Firstname, Lastname, Hobbies, Gender, Country) VALUES ('" + user1 + "','" + pass1 + "','" + fname1 + "','" + lname1 + "','" + ', '.join(hobbies) + "','" + gender + "','" + country + "')")

        # stmt = "INSERT INTO loginmaster(loginUsername,loginPassword,loginRole,loginStatus) VALUES ("{}".for)"
        # cursor1.execute(stmt)
        session['k1'] = user1
        session['k2'] = pass1
        session['k3'] = fname1
        session['k4'] = lname1
        con.commit()
        con.close()
        return render_template('login.html')

@app.route('/getsessionOne',methods=['GET','POST'])
def fn3():
    if request.method == 'POST':
        user2 = request.form.get('un1')
        pass2 = request.form.get('pw1')
        un = session['k1']
        pw = session['k2']
        if user2 == un and pass2 == pw:
            return render_template('read session2.html')
        else:
            flash('Wrong username or password')
            return redirect(url_for('login'))



@app.route('/table',methods=['GET','POST'])
def data():
    c = connection()
    cursor1=c.cursor()
    cursor1.execute("SELECT * FROM Flask2")
    data1 = cursor1.fetchall()
    print(data1)
    c.close()
    return render_template('Table.html', data1=data1)


@app.route('/delete', methods=['GET','POST'])
def deletedata():
    id = request.args.get('id')
    con=connection()
    cursor1=con.cursor()
    cursor1.execute("DELETE from Flask2 WHERE id ="+id)
    con.commit()
    con.close()
    return redirect(url_for('data'))


@app.route('/edit', methods=['GET','POST'])
def editdata():
    id = request.args.get('id')
    con=connection()
    cursor1=con.cursor()
    cursor1.execute("SELECT * FROM Flask2 WHERE id ="+id)
    edit_data=cursor1.fetchall()
    print("this is edit",edit_data)
    con.close()
    return render_template('Editdata.html',edit_data=edit_data)

@app.route('/editinsertion',methods=['GET','POST'])
def edit_data_insertion():
        user1 = request.form.get('un')
        pass1 = request.form.get('pw')
        fname1 = request.form.get('fn')
        lname1 = request.form.get('ln')
        gender = request.form['gender']
        hobbies = request.form.getlist('Hobby1')
        country = request.form.get('country')
        id1 = request.args.get('id')
        print("this",id1,fname1,lname1,user1,pass1,country,gender,'.'.join(hobbies))
        con=connection()
        cursor1=con.cursor()
        sql=( "UPDATE Flask2 SET Username = %s,Password=%s, Firstname=%s, Lastname=%s, Hobbies=%s, Gender=%s, Country=%s WHERE id=%s")
        val=(user1,pass1,fname1,lname1,','.join(hobbies),gender,country,id1)
        cursor1.execute(sql,val)
        con.commit()
        con.close()
        return redirect(url_for('data'))
app.run(threaded=True, port=9000, debug=True)