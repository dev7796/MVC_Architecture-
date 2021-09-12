import json
import os

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import CategoryVO, SubCategoryVO, ProductVO


def admin_load_product(request):
    try:
        category_vo_list = CategoryVO.objects.all()
        context = {'category_vo_list': category_vo_list}
        return render(request, "admin/addProduct.html", context)
    except Exception as ex:
        print("in admin_load_product function exception occured>>>>>", ex)


def admin_ajax_subcategory_product(request):
    try:
        category_id = request.GET.get('productCategoryId')
        category_vo = CategoryVO.objects.get(category_id=category_id)
        subcategory_vo_list = SubCategoryVO.objects.get(subcategory_category_vo=category_vo)
        subcategory_vo_dict = model_to_dict(subcategory_vo_list)
        print("in ajax_subcategory_product function subcategory_vo_dict>>>>>>>>>>>", subcategory_vo_dict)
        dump = json.dumps([subcategory_vo_dict])
        return HttpResponse(dump, content_type='application/json')
    except Exception as ex:
        print("in ajax_subcategory_product function exception occured>>>>>", ex)


def admin_insert_product(request):
    try:
        product_vo = ProductVO()

        product_category_id = request.POST.get("productCategoryId")
        product_subcategory_id = request.POST.get("productSubcategoryId")
        product_vo.product_name = request.POST.get("productName")
        product_vo.product_description = request.POST.get("productDescription")
        product_vo.product_quantity = request.POST.get("productQuantity")
        product_vo.product_price = request.POST.get("productPrice")
        product_vo.product_image = request.FILES["productImage"]
        category_vo = CategoryVO.objects.get(category_id=product_category_id)
        subcategory_vo = SubCategoryVO.objects.get(subcategory_id=product_subcategory_id)
        product_vo.product_category_vo = category_vo
        product_vo.product_subcategory_vo = subcategory_vo
        product_vo.save()
        return redirect('/admin/view_product')
    except Exception as ex:
        print("in admin_insert_product function exception occured>>>>>", ex)


def admin_view_product(request):
    try:
        product_vo_list = ProductVO.objects.select_related('product_category_vo').select_related(
            'product_subcategory_vo').all()
        return render(request, "admin/viewProduct.html", context={'product_vo_list': product_vo_list})
    except Exception as ex:
        print("in admin_view_product function exception occured>>>>>", ex)


def admin_delete_product(request):
    product_id = request.GET.get('productId')
    product_vo = ProductVO.objects.get(product_id=product_id)
    os.remove("media/" + str(product_vo.product_image))
    product_vo.delete()
    return redirect('/admin/view_product')


def admin_edit_product_data(request):
    product_id = request.GET.get('productId')
    category_vo_list = CategoryVO.objects.all()
    product_vo_list = ProductVO.objects.filter(product_id=product_id)
    context = {"product_vo_list": product_vo_list, 'category_vo_list': category_vo_list}
    return render(request, "admin/editProductData.html", context)


def admin_update_product_data(request):
    product_id = request.POST.get('productId')
    category = request.POST.get("productCategoryId")
    subcategory = request.POST.get("productSubcategoryId")
    category_vo = CategoryVO.objects.get(category_id=category)
    subcategory_vo = SubCategoryVO.objects.get(subcategory_id=subcategory)
    product_vo = ProductVO.objects.get(product_id=product_id)
    product_vo.product_name = request.POST.get("productName")
    product_vo.product_description = request.POST.get("productDescription")
    product_vo.product_quantity = request.POST.get("productQuantity")
    product_vo.product_price = request.POST.get("productPrice")
    product_vo.product_category_id = category_vo
    product_vo.product_subcategory_id = subcategory_vo
    product_vo.save()
    return redirect('/admin/view_product')


def admin_edit_product_image(request):
    product_id = request.GET.get('productId')
    product_vo_list = ProductVO.objects.filter(product_id=product_id)
    context = {"product_vo_list": product_vo_list}
    return render(request, "admin/editProductImage.html", context)


def admin_update_product_image(request):
    product_id = request.POST.get('productId')
    product_image = request.FILES['productImage']
    product_vo = ProductVO.objects.get(product_id=product_id)
    os.remove("media/" + str(product_vo.product_image))
    product_vo.product_image = product_image
    product_vo.save()
    return redirect('/admin/view_product')
