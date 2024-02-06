from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)# Текущая корзина извлекается из сеанса
    if request.method == 'POST':# В базе создается заказ
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            #очистить корзину
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()# содается экземпляр формы и прорисовывается шаблон
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})



