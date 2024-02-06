import os
from celery import Celery


#Задать стандартный модуль настроек Django для программы 'celery'
os.environ.setdefault('DJANG0_SETTINGS_MODULE', 'myshop.settings')# для встроенной в celery командной строки
app = Celery('myshop')# Создается экземпляр приложения
app.config_from_object('django.conf:settings', namespace='CELERY')# Загружается любая конфигурация из проекта и префикс для Celery
app.autodiscover_tasks()# Ищет файл tasks.py в каждом приложении и автоматически обнаруживает асинхронные задания