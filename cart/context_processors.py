from .cart import Cart


def cart(request): # Создается экземпляр класса Cart и обеспечивается доступность к данным request-а через переменную cart
    return {'cart': Cart(request)}
