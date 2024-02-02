from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        # Инициализировать корзину
        self.session = request.session #Сохранение текущего сеанса
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):#quantity - количество товара, по дефолту равно 1
        # Добавить товар в корзину или обновить его количество
        product_id = str(product.id)# конвертация в строку тк django использует json
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Пометить сеанс как измененный ч тобы обеспечить его сохранение
        self.session.modified = True

    def remove(self, product):
        # Удалить товар из корзины
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # Прокрутить товарные позиции корзины в цикле и получить товары из базы данных
        product_ids = self.cart.keys()
        # Получить объекты product и добавить их в корзину
        products = Product.objects.filter(id_in=product_ids)
        cart = self.cart.copy()# Копируем корзину в cart
        for product in products:
            cart[str(product.id)]['product'] = product # Добавляем в cart экземпляры класса Product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


