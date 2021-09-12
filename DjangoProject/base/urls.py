from django.urls import path

from . import category_view, subcategory_view, product_view, home_view

urlpatterns = [
    path('', home_view.index, name="index"),

    path('admin/load_category/', category_view.admin_load_category, name="admin_load_category"),
    path('admin/insert_category/', category_view.admin_insert_category, name="admin_insert_category"),
    path('admin/view_category/', category_view.admin_view_category, name="admin_view_category"),
    path('admin/delete_category/', category_view.admin_delete_category, name="admin_delete_category"),
    path('admin/edit_category/', category_view.admin_edit_category, name="admin_edit_category"),
    path('admin/update_category/', category_view.admin_update_category, name="admin_update_category"),

    path('admin/load_subcategory/', subcategory_view.admin_load_subcategory, name="admin_load_subcategory"),
    path('admin/insert_subcategory/', subcategory_view.admin_insert_subcategory, name="admin_insert_subcategory"),
    path('admin/view_subcategory/', subcategory_view.admin_view_subcategory, name="admin_view_subcategory"),
    path('admin/delete_subcategory/', subcategory_view.admin_delete_subcategory, name="admin_delete_subcategory"),
    path('admin/edit_subcategory/', subcategory_view.admin_edit_subcategory, name="admin_edit_subcategory"),
    path('admin/update_subcategory/', subcategory_view.admin_update_subcategory, name="admin_update_subcategory"),

    path('admin/load_product/', product_view.admin_load_product, name="admin_load_product"),
    path('admin/ajax_subcategory_product/', product_view.admin_ajax_subcategory_product,
         name="admin_ajax_subcategory_product"),
    path('admin/insert_product/', product_view.admin_insert_product, name="admin_insert_product"),
    path('admin/view_product/', product_view.admin_view_product, name="admin_view_product"),
    path('admin/delete_product/', product_view.admin_delete_product, name="admin_delete_product"),
    path('admin/edit_product_data/', product_view.admin_edit_product_data, name="admin_edit_product_data"),
    path('admin/update_product_data/', product_view.admin_update_product_data, name="admin_update_product_data"),
    path('admin/edit_product_image/', product_view.admin_edit_product_image, name="admin_edit_product_image"),
    path('admin/update_product_image/', product_view.admin_update_product_image, name="admin_update_product_image")
]
