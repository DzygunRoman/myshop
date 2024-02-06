import os
from celery import Celery


#Задать стандартный модуль настроек Django для программы 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')# для встроенной в celery командной строки
app = Celery('myshop')# Создается экземпляр приложения
app.config_from_object('django.conf:settings', namespace='CELERY')# Загружается любая конфигурация из проекта и префикс для Celery
app.autodiscover_tasks()# Ищет Celery Wordjango.core.exceptions.ImproperlyConfigured: Requested settings, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.kerфайл tasks.py в каждом приложении и автоматически обнаруживает асинхронные задания