import sys
sys.dont_write_bytecode = True

from django.db import models
from django.contrib.auth import get_user_model

class OutputTagModel(models.Model):

    tag = models.CharField(
        verbose_name = 'タグ',
        max_length = 100,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique = True,
    )

    def __str__(self):
        return self.tag


class Output(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    question = models.TextField(
        verbose_name='質問',
        null=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name='内容'
    )

    created_at = models.DateTimeField(
        verbose_name = '投稿日',
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        verbose_name = '更新日',
        auto_now = True
    )

    tags = models.ManyToManyField(
        OutputTagModel,
    )

    def __str__(self):
        return self.description[:10]