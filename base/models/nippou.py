import sys
sys.dont_write_bytecode = True

from django.db import models
from django.contrib.auth import get_user_model

class Nippou(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    sales = models.PositiveIntegerField(
        verbose_name='販売個数',
        default=0,
    )

    revenue = models.PositiveBigIntegerField(
        verbose_name='利益',
        default=0,
    )

    plan = models.TextField(
        verbose_name='その他',
        default='',
        null=True,
        blank=True,
    )

    date = models.DateField(
        verbose_name = '対象日'
    )

    def __str__(self):
        return str(self.date) + 'の日報'