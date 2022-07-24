from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
import sys
sys.dont_write_bytecode = True

STYLE = (('real', 'リアルミーティング'), ('Zoom', 'Zoom'))
ENTRY = (('real', '参加'), ('online', 'オンライン参加'), ('nonentry', '不参加'))
PARTY_ENTRY = (('entry', '参加'), ('nonentry', '不参加'))


class Plan(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=50)
    style = models.CharField(verbose_name='開催形態', max_length=50, choices=STYLE)
    zoom_link = models.URLField(verbose_name='Zoomリンク')
    open_date = models.DateField(verbose_name='開催日')
    start_time = models.TimeField(verbose_name='開始時刻')
    end_time = models.TimeField(verbose_name='終了予定時刻')
    party_time = models.TimeField(verbose_name='懇親会日時', blank=True, null=True)
    description = models.CharField(verbose_name='内容', max_length=1000)

    def __str__(self):
        return self.title

class PlanReply(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
    )
    entry = models.CharField(
        verbose_name='参加・不参加',
        max_length=50,
        choices=ENTRY,
        blank = True,
        null = True
    )
    party = models.CharField(
        verbose_name='懇親会',
        max_length=10,
        choices=PARTY_ENTRY,
        blank = True,
        null = True
    )
    status = models.CharField(
        verbose_name='状況',
        max_length=200,
        blank = True,
        null = True
    )
    desired = models.CharField(
        verbose_name='希望の内容',
        max_length=200,
        blank = True,
        null = True
    )
    question = models.CharField(
        verbose_name='質問・お悩み',
        max_length=500,
        blank = True,
        null = True
    )
    to_ayaka = models.CharField(
        verbose_name='梅野に聞きたいこと',
        max_length=500,
        blank = True,
        null = True
    )
    others = models.CharField(
        verbose_name='その他要望',
        max_length=500,
        blank = True,
        null = True
    )

    def __str__(self):
        return self.user.profile.name