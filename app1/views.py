from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.db.models import Q

from app1.models import Cart, Product
def home(request):
    return render(request,'home.html')
class CategoryView(View):
    def get(self,request,val):
        product =Product.objects.filter(category=val)
        return render(request,"category.html",locals())
def all(request):
    pro=Product.objects.all()
    return render(request,'all.html',{'pro':pro})

def product_details(request,pk):
    product =Product.objects.get(id=pk)
    return render(request,"product_details.html",{'i':product})
'''def add_cart(request):
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(product=product).save()
    return redirect("/show_cart")'''


def add_cart(request):
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.all()
    '''for i in cart:
        if i.product==product:
            return redirect("/show_cart")
        else:'''
    Cart(product=product).save()
    return redirect("/show_cart")
def show_cart(request):
    cart_items = Cart.objects.all()
    amount = 0
    for p in cart_items:
        if p.quantity and p.product and p.product.discounted_price:
            value = p.quantity * p.product.discounted_price
            amount += value
    totalamount = amount + 40
    return render(request, 'cart.html', {'cart_items': cart_items,'totalamount': totalamount,
        'amount': amount})
'''def show_cart(request,pk):
    product=Cart.objects.get(id=pk)
    cart=Cart.objects.filter(product=product)
    return render(request, 'add_cart.html',{'product':product})'''
def remove_pro(request,pk):
    s=Cart.objects.get(id=pk)
    s.delete()
    return redirect('/show_cart/')
def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id))
        c.quantity+=1
        c.save()
        cart_items= Cart.objects.all()
        amount = 0
        for p in cart_items:
            if p.quantity and p.product and p.product.discounted_price:
                value = p.quantity * p.product.discounted_price
                amount += value
        totalamount = amount + 40
        #print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,

        }
        return JsonResponse(data)
def add_quantity(request,pk):
    c=Cart.objects.get(id=pk)
    c.quantity+=1
    c.save()
    return redirect('/show_cart')
def remove_quantity(request,pk):
    c=Cart.objects.get(id=pk)
    if c.quantity>1:
        c.quantity-=1
        c.save()
    else:
        c.quantity=1
    return redirect('/show_cart')


# Create your views here.
