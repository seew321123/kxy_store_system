from django.shortcuts import render
from .models import Product,Store
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request,'kxy_store/index.html')

@login_required
def stores(request):
    stores = Store.objects.order_by('date_added')
    context = {'stores':stores}
    return render(request,'kxy_store/stores.html',context)

@login_required
def store(request,store_id):
    store = Store.objects.get(id = store_id)
    #products = store.product_set.order_by('id')
    products = Product.objects.filter(store = store).order_by('id')
    cotext = {'store':store,'products':products}
    return render(request,'kxy_store/store.html',cotext)

@login_required
def search(request,store_id):
    store = Store.objects.get(id=store_id)
    #products = Product.objects.filter(Q(store = store) | Q(text__startswith='bv')).order_by('id')
    if request.method != 'POST':
        pass
    else:
        kw = request.POST.get('kw')
        if kw:
            products = store.product_set.filter(text__contains=kw).order_by('id')
    context = {'store': store,'products':products}
    return render(request, 'kxy_store/store.html', context)

def edit(request,product_id):
    product = Product.objects.get(id=product_id)
    store = product.store
    if request.method != 'POST':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kxy_store:store',args=[store.id]))
    context = {'product':product,'store':store,'form':form}
    return render(request,'kxy_store/edit.html',context)

def add(request,store_id):
    store = Store.objects.get(id=store_id)
    if request.method != 'POST':
        form = ProductForm()
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kxy_store:store',args=[store.id]))
    context = {'store':store,'form':form}
    return render(request,'kxy_store/add.html',context)

def delete(request,product_id):
    product = Product.objects.get(id=product_id)
    store = product.store
    Product.objects.get(id=product_id).delete()
    return HttpResponseRedirect(reverse('kxy_store:store',args=[store.id]))

