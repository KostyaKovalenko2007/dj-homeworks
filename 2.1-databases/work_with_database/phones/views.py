from django.shortcuts import render, redirect,get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'id')
    ordering = {'id':'id','name':'name', 'min_price':'price','max_price':'-price'}
    phones = Phone.objects.all().order_by(ordering[sort]).values()
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone' : phone
    }
    return render(request, template, context)
