import pydrill
import pymysql
import pymysql.cursors
from flask import *
from flask_mysqldb import MySQL
import time
import psycopg2
import traceback
import pyodbc

app = Flask(__name__)
app.secret_key = 'DevShah'
app.config['MYSQL_HOST'] = 'instacart.ck12z0ni2znt.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'cs527group7'
app.config['MYSQL_DB'] = 'instacart'
mysql = MySQL(app)

# Redshift setup
# redshift = psycopg2.connect(dbname='instacart',
#                             host='redshift-cluster-1.clypxjjaqru2.us-east-2.redshift.amazonaws.com',
#                             port='5439',
#                             user='cs527user',
#                             password='MyRedshift123')

#Mongo setup
# server = ''
# port  = 27017
# database='instacart'
#
# con = pyodbc.connect('DRIVER={Devart ODBC Driver for MongoDB};'
#                                   'Server=' + server + ';Port=' + str(port) +
#                                   ';Database=' + database)
#
# cur = con.cursor()
# cur.execute('select * from aisles')
# res = cur.fetchall()
# print(res)

@app.route('/')
def fn1():
    return render_template('index_login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('index_register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('index_login.html')

@app.route('/setsession',methods=['GET','POST'])
def setsession():
    if request.method == "POST":
        user1 = request.form.get('un')
        pass1 = request.form.get('pw')
        fname1 = request.form.get('Fn')
        lname1 = request.form.get('Ln')
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Register_User( Username , Password, Firstname, Lastname) VALUES ('" + user1 + "','" + pass1 + "','" + fname1 + "','" + lname1 + "')")
        session['k1'] = user1
        session['k2'] = pass1
        session['k3'] = fname1
        session['k4'] = lname1
        mysql.connection.commit()
        return render_template('index_login.html')

@app.route('/getsessionOne',methods=['GET','POST'])
def fn3():
    if request.method == 'POST':
        user2 = request.form.get('un1')
        pass2 = request.form.get('pw1')
        if user2 == 'admin' and pass2 == 'admin':
            return render_template('index.html')
        else:
            return render_template('index_user.html')

        # else:
        #     flash("Wrong username or password")
        #     return redirect(url_for('login'))








@app.route('/index', methods=['GET', 'POST'])
def index():
    elapsed_time = 0
    error = ''
    field_names = []
    try:
        fetchdata = ''
        if request.method == 'POST':
            print("hi")
            start_time = time.time()
            query_details = request.form
            query = query_details['my_query']
            redshift = psycopg2.connect(dbname='instacart',
                                        host='redshift-cluster-1.clypxjjaqru2.us-east-2.redshift.amazonaws.com',
                                        port='5439',
                                        user='cs527user',
                                        password='MyRedshift123')

            if query_details['options'] == 'my_mysql':
                cur = mysql.connection.cursor()
                cur.execute(query)
                mysql.connection.commit()
                fetchdata = cur.fetchall()
                fetchdata = list(fetchdata)
                field_names = [i[0] for i in cur.description]
                fetchdata.append((field_names))
                print("mysql",fetchdata)
                cur.close()
                elapsed_time = time.time() - start_time
            elif query_details['options'] == 'my_redshift':
                print("this is read")
                cur = redshift.cursor()
                cur.execute(query)
                redshift.commit()
                fetchdata = cur.fetchall()
                fetchdata = list(fetchdata)
                field_names = [i[0] for i in cur.description]
                fetchdata.append((field_names))
                print("redshift",fetchdata)
                cur.close()
                elapsed_time = time.time() - start_time
    except mysql.connect.DatabaseError:
        error = "There is an error in your SQL syntax."
    except (TypeError, AttributeError, psycopg2.ProgrammingError):
        error = "Command executed successful"
    except Exception:
        traceback.print_exc()
        error = "There is an error in your program."
    return render_template('Project11.html', data1=fetchdata, time=elapsed_time, error=error)

    elapsed_time = 0
    error = ''
    field_names = []

    fetchdata = ''
    if request.method == 'POST':
        start_time = time.time()
        query_details = request.form
        query = query_details['my_query']
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        # con = connection()
        # cur = con.cursor()
        # cur.execute(query)
        #con.commit()
        fetchdata = cur.fetchall()
        fetchdata = list(fetchdata)
        print(fetchdata)
        print(cur.description)
        field_names = [i[0] for i in cur.description]
        print("this are fieldnames", field_names)
        fetchdata.append((field_names))
        print("this is new fetch data",fetchdata)
        cur.close()
        #elapsed_time = time.time() - start_time
        return render_template('Project11.html', data1=fetchdata)


app.run(threaded=True, port=4000, debug=True)