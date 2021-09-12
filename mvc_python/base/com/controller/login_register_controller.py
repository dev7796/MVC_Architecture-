from flask import *
from base import app
from base.com.dao.login_register_dao import CategoryDAO
from base.com.vo.login_register_vo import CategoryVO
import re

@app.route("/register")
def register():
    return render_template('login_register/register_user.html')

@app.route('/login')
def login():
    return render_template('login_register/login_user.html')



@app.route('/register_user',methods=['GET','POST'])
def register_user():
    if request.method == "POST":
        category_dao = CategoryDAO()
        category_vo = CategoryVO()
        category_vo.username = request.form.get('un')
        category_vo.password = request.form.get('pw')
        category_vo.firstname = request.form.get('fn')
        category_vo.lastname = request.form.get('ln')



        regexp = re.compile('[^0-9a-zA-Z]+')
        regexp1 = re.compile('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$') # ?= Match a suffix but exclude it from capture.
        SpecialSym = ['$', '@', '#', '%']
        SpecialSym1 = ['^', '@', '+', '_']


        # Check Firstname

        if regexp.search(category_vo.firstname):
            flash("Please remove any special characters from FIRSTNAME", 'error11')
            return render_template('login_register/register_user.html')

        # Check Lastname

        if regexp.search(category_vo.lastname):
            flash("Please remove any special characters from LASTNAME", 'error12')
            return render_template('login_register/register_user.html')

        # Check Username

        if regexp.search(category_vo.username):
            flash("Please remove any special characters from USERNAME", 'error13')
            return render_template('login_register/register_user.html')

        if len(category_vo.username) < 4:
            flash('Length should be at least 4', 'error13')
            return render_template('login_register/register_user.html')

        if not (category_vo.username[0].isupper()):
            flash('Username should have first letter in uppercase','error13')
            return render_template('login_register/register_user.html')

        if not any(char.isdigit() for char in category_vo.username):
            flash('Username should have at least one numeral','error13')
            return render_template('login_register/register_user.html')

        if not any(char in SpecialSym for char in category_vo.username):
            flash('Username should have at least one of these symbols " ^ @ _ + "','error13')
            return render_template('login_register/register_user.html')

        # Check Password

        if len(category_vo.password) < 6:
            flash('Length should be at least 6','error14')
            return render_template('login_register/register_user.html')

        if len(category_vo.password) > 20:
            flash('length should be not be greater than 8','error14')
            return render_template('login_register/register_user.html')

        if not any(char.isdigit() for char in category_vo.password):
            flash('Password should have at least one numeral','error14')
            return render_template('login_register/register_user.html')

        if not any(char.isupper() for char in category_vo.password):
            flash('Password should have at least one uppercase letter','error14')
            return render_template('login_register/register_user.html')

        if not any(char.islower() for char in category_vo.password):
            flash('Password should have at least one lowercase letter','error14')
            return render_template('login_register/register_user.html')

        if not any(char in SpecialSym for char in category_vo.password):
            flash('Password should have at least one of the symbols $@#','error14')
            return render_template('login_register/register_user.html')

        else:
            category_dao.register_user(category_vo)
            return redirect(url_for('home'))



@app.route('/login_user',methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        category_dao = CategoryDAO()
        category_vo = CategoryVO()
        category_vo.username = request.form.get('un1')
        category_vo.password = request.form.get('pw1')
        user_data = category_dao.login_user(category_vo)
        print(user_data[0])
        if len(user_data) == 0:
            flash('Wrong username or password')
            return redirect(url_for('login'))
        elif user_data[0]['username'] == category_vo.username and user_data[0]['password'] == category_vo.password:
            return render_template('admin/home.html')
        elif user_data[0]['username'] == category_vo.username and user_data[0]['password'] != category_vo.password:
            flash('Wrong password', 'error1')
            return redirect(url_for('login'))
        else:
            flash('Wrong username', 'error')
            return redirect(url_for('login'))



