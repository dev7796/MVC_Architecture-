from django.contrib import messages
from django.shortcuts import render, redirect

from .models import CategoryVO


def admin_load_category(request):
    try:
        return render(request, "admin/addCategory.html")
    except Exception as ex:
        print("in admin_load_category function exception occured>>>>>", ex)


def admin_insert_category(request):
    try:
        category_vo = CategoryVO()
        category_vo.category_name = request.POST.get('categoryName')
        category_vo.category_description = request.POST.get('categoryDescription')
        category_vo.save()
        messages.info(request, 'Category insert successfully!')
        return redirect("/admin/view_category")
    except Exception as ex:
        print("in admin_insert_category function exception occured>>>>>", ex)


def admin_view_category(request):
    try:
        category_vo_list = CategoryVO.objects.all()
        print("category_vo_list>>>>>>>>>", category_vo_list)
        return render(request, 'admin/viewCategory.html', context={'category_vo_list': category_vo_list})
    except Exception as ex:
        print("in admin_view_category function exception occured>>>>>", ex)



def admin_delete_category(request):
    try:
        category_id = request.GET.get('categoryId')
        print("category_id>>>>>>>", category_id)
        category_vo = CategoryVO.objects.get(category_id=category_id)
        category_vo.delete()
        messages.info(request, 'Category remove successfully!')
        return redirect("/admin/view_category")
    except Exception as ex:
        print("in admin_delete_category function exception occured>>>>>", ex)



def admin_edit_category(request):
    try:
        category_id = request.GET.get('categoryId')
        category_vo_list = CategoryVO.objects.filter(category_id=category_id)
        print("category_vo_list>>>>>>>>>", category_vo_list)
        return render(request, "admin/editCategory.html", context={'category_vo_list': category_vo_list})
    except Exception as ex:
        print("in admin_edit_category function exception occured>>>>>", ex)



def admin_update_category(request):
    try:
        category_id = request.POST.get('categoryId')
        category_name = request.POST.get('categoryName')
        category_description = request.POST.get('categoryDescription')

        print("category_id>>>>>>>>", category_id)
        print("category_name>>>>>>", category_name)
        print("category_description>>>>>>>>>>", category_description)

        category_vo = CategoryVO.objects.get(category_id=category_id)
        category_vo.category_name = category_name
        category_vo.category_description = category_description
        print("category_vo>>>>>>>>>>>>>", category_vo)
        category_vo.save()
        messages.info(request, 'Category update successfully!')
        return redirect("/admin/view_category")
    except Exception as ex:
        print("in admin_update_category function exception occured>>>>>", ex)
