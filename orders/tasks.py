import sys

from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    #Задание по отправке уведомления по электронной почте при успешном создании заказа.
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = (f'Дорогой {order.first_name},\n\n '
               f'Ваш заказ успешно размещен.'
               f'Номер вашего заказа {order.id}.')
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    if order_id == False:
        sys.exit('Abort!')
    return mail_sent

