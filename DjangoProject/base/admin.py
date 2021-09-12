from django.contrib import admin

from .models import CategoryVO, SubCategoryVO, ProductVO, UserVO, LoginVO

# Register your models here.
admin.site.register(LoginVO)
admin.site.register(UserVO)
admin.site.register(CategoryVO)
admin.site.register(SubCategoryVO)
admin.site.register(ProductVO)
