import random

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, DateTimeField, FileField, PROTECT, CASCADE, TextField, OneToOneField
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


class UGCMixin(models.Model):
    author = ForeignKey(to=get_user_model(), on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(models.Model):
    user: User = OneToOneField(to=get_user_model(), on_delete=CASCADE)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    birth_year = models.fields.PositiveSmallIntegerField(max_length=4, null=True, blank=True)

    description = models.fields.TextField(null=True, verbose_name='Description', blank=True)

    country = CountryField(null=True)

    avatar = FileField(upload_to='avatars', null=True)

    @property
    def get_presence_status(self):
        return True

    @property
    def display_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username} - id:{self.user.id})"



class Video(UGCMixin):
    file = FileField(upload_to='videos')

    def __str__(self):
        return f"{self.author} ({self.id}) -> ({self.dream_set.first()})"


class Dream(UGCMixin):
    title = models.fields.TextField()
    description = models.fields.TextField(null=True, verbose_name='Description', blank=True)
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    active = models.fields.BooleanField(default=False)

    media = ForeignKey(to=Video, null=True, blank=True, on_delete=CASCADE)

    @property
    def get_progress(self):
        return random.randint(10, 87)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Vote(UGCMixin):
    class Meta:
        unique_together = ('author', 'object_id', 'content_type')

    POSITIVE = 1
    NEGATIVE = 2

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')

    value = models.fields.PositiveSmallIntegerField(
        choices=(
            (POSITIVE, 'Positive'),
            (NEGATIVE, 'Negative')
        )
    )


class Donation(UGCMixin):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    purpose = ForeignKey(to=Dream, on_delete=PROTECT)
    comment = TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} for {self.purpose}"
