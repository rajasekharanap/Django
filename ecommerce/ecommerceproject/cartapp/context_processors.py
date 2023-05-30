from. models import Cart,Cartitem
from .views import _cart_id

def counter(request):
    itemcount=0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart=Cart.objects.filter(cartid=_cart_id(request))
            citem=Cartitem.objects.all().filter(cart=cart[:1])
            for i in citem:
                itemcount+=i.quantity
        except Cart.DoesNotExist:
            itemcount=0
    return dict(itemcount=itemcount)
