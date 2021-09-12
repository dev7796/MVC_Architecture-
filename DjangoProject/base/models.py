from django.db import models


# Create your models here.
class CategoryVO(models.Model):
    category_id = models.AutoField(db_column="category_id", primary_key=True, null=False)
    category_name = models.CharField(db_column="category_name", max_length=30, default="", null=False)
    category_description = models.CharField(db_column="category_description", max_length=100, default="", null=False)

    def __str__(self):
        return '{} {}'.format(self.category_name, self.category_description)

    class Meta:
        db_table = "category_table"


class SubCategoryVO(models.Model):
    subcategory_id = models.AutoField(db_column="subcategory_id", primary_key=True, null=False)
    subcategory_name = models.CharField(db_column="subcategory_name", max_length=30, default="", null=False)
    subcategory_description = models.CharField(db_column="subcategory_description", max_length=30, default="",
                                               null=False)
    subcategory_category_vo = models.ForeignKey(CategoryVO, on_delete=models.CASCADE,
                                                db_column="subcategory_category_id")

    def __str__(self):
        return '{} {}'.format(self.subcategory_name, self.subcategory_description)

    class Meta:
        db_table = "subcategory_table"


class ProductVO(models.Model):
    product_id = models.AutoField(db_column="product_id", primary_key=True, null=False)
    product_name = models.CharField(db_column="product_name", max_length=50, default="", null=False)
    product_description = models.CharField(db_column="product_description", max_length=500, default="", null=False)
    product_quantity = models.IntegerField(db_column="product_quantity", null=False)
    product_price = models.IntegerField(db_column="product_price", null=False)
    product_image = models.ImageField(upload_to='images/', db_column="product_image")
    product_category_vo = models.ForeignKey(CategoryVO, on_delete=models.CASCADE, db_column="product_category_id")
    product_subcategory_vo = models.ForeignKey(SubCategoryVO, on_delete=models.CASCADE,
                                               db_column="product_subcategory_id")

    def __str__(self):
        return '{} {} {} {}'.format(self.product_name, self.product_description, self.product_quantity,
                                    self.product_price)

    class Meta:
        db_table = "product_table"


class LoginVO(models.Model):
    login_id = models.AutoField(db_column="login_id", primary_key=True, null=False)
    login_email = models.CharField(db_column="login_email", max_length=200, default="", null=False)
    login_password = models.CharField(db_column="login_password", max_length=200, default="", null=False)
    login_role = models.CharField(db_column="login_role", max_length=10, default="", null=False)
    login_secretkey = models.CharField(db_column="login_secretkey", max_length=200, default="", null=False)
    login_status = models.CharField(db_column="login_status", max_length=10, default="", null=False)

    def __str__(self):
        return '{} {} {} {}'.format(self.login_email, self.login_password, self.login_role,
                                    self.login_secretkey)

    class Meta:
        db_table = "login_table"


class UserVO(models.Model):
    user_id = models.AutoField(db_column="user_id", primary_key=True, null=False)
    user_firstname = models.CharField(db_column="user_firstname", max_length=200, default="", null=False)
    user_lastname = models.CharField(db_column="user_lastname", max_length=200, default="", null=False)
    user_gender = models.CharField(db_column="user_gender", max_length=10, default="", null=False)
    user_address = models.CharField(db_column="user_address", max_length=200, default="", null=False)
    user_country = models.CharField(db_column="user_country", max_length=10, default="", null=False)
    user_hobby = models.CharField(db_column="user_hobby", max_length=50, default="", null=False)
    user_login_id = models.ForeignKey(LoginVO, on_delete=models.CASCADE, db_column="user_login_id")

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.user_firstname, self.user_lastname, self.user_gender,
                                          self.user_address, self.user_country, self.user_hobby)

    class Meta:
        db_table = "user_table"
