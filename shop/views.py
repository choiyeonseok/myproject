from django.shortcuts import render, redirect

from shop.models import Product


def index(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products})

    elif request.method == 'POST':
        name = request.POST['name']
        contents = request.POST['contents']
        photo = request.FILES.get('photo', False)
        Product.objects.create(name=name,
                               contents=contents,
                               photo=photo)
        return redirect('/shop')


def new(request):
    return render(request, 'shop/new.html')
