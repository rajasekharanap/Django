from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart,Cartitem
from ecommerceapp.models import Product
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,prod_id):
    prod=Product.objects.get(id=prod_id)
    try:
        cart=Cart.objects.get(cartid=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cartid=_cart_id(request))
        cart.save()
    try:
        cart_item=Cartitem.objects.get(product=prod,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
            cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item=Cartitem.objects.create(product=prod,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cartapp:cartdetails')


def cartdetails(request,total=0,counter=0,cartitems=None):
    try:
        cart=Cart.objects.get(cartid=_cart_id(request))
        cartitems=Cartitem.objects.filter(cart=cart,active=True)
        for i in cartitems:
            total+=i.product.price*i.quantity
            counter+=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartitems=cartitems,total=total,counter=counter))

def cartdelete(request,prod_id):
    cart=Cart.objects.get(cartid=_cart_id(request))
    product=get_object_or_404(Product,id=prod_id)
    cartitem=Cartitem.objects.get(product=product,cart=cart)
    if cartitem.quantity > 1:
        cartitem.quantity-=1
        cartitem.save(),
    else:
        cartitem.delete()
    return redirect('cartapp:cartdetails')

def cartremove(request,prod_id):
    cart=Cart.objects.get(cartid=_cart_id(request))
    product=get_object_or_404(Product,id=prod_id)
    cartitem=Cartitem.objects.get(product=product,cart=cart)
    cartitem.delete()
    return redirect('cartapp:cartdetails')