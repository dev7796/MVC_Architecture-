# Generated by Django 3.1 on 2020-10-13 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryVO',
            fields=[
                ('category_id', models.AutoField(db_column='category_id', primary_key=True, serialize=False)),
                ('category_name', models.CharField(db_column='category_name', default='', max_length=30)),
                ('category_description', models.CharField(db_column='category_description', default='', max_length=100)),
            ],
            options={
                'db_table': 'category_table',
            },
        ),
        migrations.CreateModel(
            name='LoginVO',
            fields=[
                ('login_id', models.AutoField(db_column='login_id', primary_key=True, serialize=False)),
                ('login_email', models.CharField(db_column='login_email', default='', max_length=200)),
                ('login_password', models.CharField(db_column='login_password', default='', max_length=200)),
                ('login_role', models.CharField(db_column='login_role', default='', max_length=10)),
                ('login_secretkey', models.CharField(db_column='login_secretkey', default='', max_length=200)),
                ('login_status', models.CharField(db_column='login_status', default='', max_length=10)),
            ],
            options={
                'db_table': 'login_table',
            },
        ),
        migrations.CreateModel(
            name='UserVO',
            fields=[
                ('user_id', models.AutoField(db_column='user_id', primary_key=True, serialize=False)),
                ('user_firstname', models.CharField(db_column='user_firstname', default='', max_length=200)),
                ('user_lastname', models.CharField(db_column='user_lastname', default='', max_length=200)),
                ('user_gender', models.CharField(db_column='user_gender', default='', max_length=10)),
                ('user_address', models.CharField(db_column='user_address', default='', max_length=200)),
                ('user_country', models.CharField(db_column='user_country', default='', max_length=10)),
                ('user_hobby', models.CharField(db_column='user_hobby', default='', max_length=50)),
                ('user_login_id', models.ForeignKey(db_column='user_login_id', on_delete=django.db.models.deletion.CASCADE, to='base.loginvo')),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryVO',
            fields=[
                ('subcategory_id', models.AutoField(db_column='subcategory_id', primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(db_column='subcategory_name', default='', max_length=30)),
                ('subcategory_description', models.CharField(db_column='subcategory_description', default='', max_length=30)),
                ('subcategory_category_vo', models.ForeignKey(db_column='subcategory_category_id', on_delete=django.db.models.deletion.CASCADE, to='base.categoryvo')),
            ],
            options={
                'db_table': 'subcategory_table',
            },
        ),
        migrations.CreateModel(
            name='ProductVO',
            fields=[
                ('product_id', models.AutoField(db_column='product_id', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='product_name', default='', max_length=50)),
                ('product_description', models.CharField(db_column='product_description', default='', max_length=500)),
                ('product_quantity', models.IntegerField(db_column='product_quantity')),
                ('product_price', models.IntegerField(db_column='product_price')),
                ('product_image', models.ImageField(db_column='product_image', upload_to='images/')),
                ('product_category_vo', models.ForeignKey(db_column='product_category_id', on_delete=django.db.models.deletion.CASCADE, to='base.categoryvo')),
                ('product_subcategory_vo', models.ForeignKey(db_column='product_subcategory_id', on_delete=django.db.models.deletion.CASCADE, to='base.subcategoryvo')),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
    ]