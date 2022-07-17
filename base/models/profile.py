import sys
sys.dont_write_bytecode = True

from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        unique=True,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    name = models.CharField(
        default='ウメカリメンバー',
        max_length=30,
    )

    icon = models.ImageField(
        verbose_name='アイコン',
        null=True,
        blank=True,
    )

    introduction = models.TextField(
        verbose_name='自己紹介',
        null=True,
        blank=True,
    )

    target = models.PositiveIntegerField(
        verbose_name='目標金額',
        default=0,
    )

    dream = models.ImageField(
        verbose_name='ビジョンボード',
        null=True,
        blank=True,
    )