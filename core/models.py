from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, DateTimeField, FileField, PROTECT, CASCADE, TextField
from djmoney.models.fields import MoneyField


class UGCMixin(object):
    author = ForeignKey(to=get_user_model(), on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Video(models.Model, UGCMixin):
    file = FileField(upload_to='videos')


class Dream(models.Model, UGCMixin):
    description = models.fields.TextField(null=True, verbose_name='Description')
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    media = ForeignKey(to=Video, on_delete=CASCADE)


class Vote(models.Model, UGCMixin):
    value = models.fields.PositiveSmallIntegerField(
        choices=(
            (1, 'Positive'),
            (2, 'Negative')
        )
    )


class Donation(models.Model, UGCMixin):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    purpose = ForeignKey(to=Dream, on_delete=PROTECT)
    comment = TextField(blank=True, null=True)
