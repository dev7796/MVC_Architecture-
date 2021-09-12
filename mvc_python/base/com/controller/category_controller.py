from flask import *
from base import app
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route('/')
def home():
    return render_template('admin/home.html')


@app.route('/load_category')
def load_category():
    return render_template('admin/load_category.html')

@app.route('/view_table')
def view_table():
    return render_template('admin/view_category.html')


@app.route('/insert_category',methods=['post'])
def insert_category():
    category_name=request.form.get('category_name')
    category_description=request.form.get('category_description')
    print(category_name,category_description)

    category_dao=CategoryDAO()
    category_vo=CategoryVO()

    category_vo.category_name=category_name
    category_vo.category_description=category_description


    category_dao.insert_category(category_vo)


    return redirect(url_for('home'))

@app.route('/view_category')
def view_category():
    category_dao = CategoryDAO()
    view_table = category_dao.view_category()
    return render_template('admin/view_category.html', data1=view_table)


@app.route('/delete_category')
def delete_category():
    category_dao = CategoryDAO()
    category_vo = CategoryVO()
    category_vo.category_id = request.args.get('id')
    print(category_vo.category_id)
    category_dao.delete_category(category_vo)
    return redirect(url_for('view_category'))


@app.route('/edit_category')
def edit_category():
    category_dao = CategoryDAO()
    category_vo = CategoryVO()
    category_vo.category_id = request.args.get('id')
    print(category_vo.category_id)
    edited_data = category_dao.edit_category(category_vo)
    return render_template('admin/edit_category.html', edit_data=edited_data)

@app.route('/update_category' , methods=['GET','POST'])
def update_category():
        print("hi")
        category_dao = CategoryDAO()
        category_vo = CategoryVO()
        category_vo.category_name = request.form.get('category_name')
        category_vo.category_description = request.form.get('category_description')
        category_vo.category_id = request.args.get('id')
        print(category_vo.category_id, category_vo.category_description, category_vo.category_name)
        category_dao.update_category(category_vo)
        return redirect(url_for('view_category'))


