from flask import *
from base import app
import re
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO
from base.com.dao.subcategory_dao import SubcategoryDAO
from base.com.vo.subcategory_vo import SubcategoryVO


@app.route('/load_subcategory')
def load_subcategory():
    category_dao = CategoryDAO()
    view_table = category_dao.load_subcategory()
    return render_template('subcategory/load_subcategory.html', data1=view_table)


@app.route('/insert_subcategory', methods=['GET','POST'])
def insert_subcategory():
    subcategory_name = request.form.get('subcategory_name')
    subcategory_description = request.form.get('subcategory_description')
    subcategory_category_id = request.form.get('subcategory')
    print(subcategory_name, subcategory_description, subcategory_category_id)

    subcategory_dao = SubcategoryDAO()
    subcategory_vo = SubcategoryVO()

    subcategory_vo.subcategory_name = subcategory_name
    subcategory_vo.subcategory_description = subcategory_description
    subcategory_vo.subcategory_category_id = subcategory_category_id


    regexp = re.compile('[^0-9a-zA-Z]+')
    if regexp.search(subcategory_name):
        flash("Please remove any special characters", 'error1')
        return redirect(url_for('load_subcategory'))
    else:
        subcategory_dao.insert_subcategory(subcategory_vo)
        return redirect(url_for('home'))

@app.route('/view_subcategory')
def view_subcategory():
    subcategory_dao = SubcategoryDAO()
    view_table = subcategory_dao.view_subcategory()
    return render_template('subcategory/view_subcategory.html', data1=view_table)

@app.route('/delete_subcategory')
def delete_subcategory():
    subcategory_dao = SubcategoryDAO()
    subcategory_vo = SubcategoryVO()
    subcategory_vo.subcategory_id = request.args.get('id')
    print(subcategory_vo.subcategory_id)
    subcategory_dao.delete_subcategory(subcategory_vo)
    return redirect(url_for('view_subcategory'))


@app.route('/edit_subcategory')
def edit_subcategory():
    subcategory_dao = SubcategoryDAO()
    subcategory_vo = SubcategoryVO()
    subcategory_vo.subcategory_id = request.args.get('id')

    edited_data = subcategory_dao.edit_subcategory(subcategory_vo)
    return render_template('subcategory/edit_subcategory.html', edit_data=edited_data)

@app.route('/update_subcategory' , methods=['GET','POST'])
def update_subcategory():
        subcategory_dao = SubcategoryDAO()
        subcategory_vo = SubcategoryVO()
        subcategory_vo.subcategory_name = request.form.get('subcategory_name')
        subcategory_vo.subcategory_description = request.form.get('subcategory_description')
        subcategory_vo.subcategory_id = request.args.get('id')
        print(subcategory_vo.subcategory_id, subcategory_vo.subcategory_description, subcategory_vo.subcategory_name)
        subcategory_dao.update_subcategory(subcategory_vo)
        return redirect(url_for('view_subcategory'))