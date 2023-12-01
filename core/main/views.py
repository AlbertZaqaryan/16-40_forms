from django.shortcuts import render, redirect
from .models import Category, SubCategory, Product, Support
# Create your views here.

def index(request):
    category_list = Category.objects.all()
    return render(request, 'index.html', context={
        'category_list':category_list
    })



def index_detail(request, id):
    sub_category_list = Category.objects.filter(pk=id)
    return render(request, 'index_detail.html', context={
        'sub_category_list':sub_category_list
    })

def product_pge(request, id):
    product_list = SubCategory.objects.filter(pk=id)
    return render(request, 'product_page.html', context={
        'product_list':product_list
    })


def support(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        Support.objects.create(name=user_name, email=user_email, message=user_message)
        return redirect('index')
    return render(request, 'support.html', context={

    })
