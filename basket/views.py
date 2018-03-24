from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .basket import basket
from .forms import BasketAddProductForm

# def basket(request):
#     return render(request, 'basket.html')

@require_POST
def BasketAdd(request, product_id):
    Basket = basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        Basket.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('Basket:BasketDetail')

def BasketRemove(request, product_id):
    Basket = basket(request)
    product = get_object_or_404(Product, id=product_id)
    Basket.remove(product)
    return redirect('Basket:BasketDetail')

def BasketDetail(request):
    Basket = basket(request)
    return render(request, 'basket/basket.html', {'Basket': Basket})
