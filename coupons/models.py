from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='Код')
    valid_from = models.DateTimeField(verbose_name='Действителен с ')
    valid_to = models.DateTimeField(verbose_name='Действителен до ')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],help_text='Значение в процентах (0 до 100)')
    active = models.BooleanField(verbose_name='Cтатус')

    def __str__(self):
        return self.code

