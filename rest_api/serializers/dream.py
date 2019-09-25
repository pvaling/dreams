from django.db.migrations.serializer import DecimalSerializer
from moneyed import Money
from rest_framework import serializers
from rest_framework.fields import DecimalField
from rest_framework.serializers import ModelSerializer

from core.models import Dream


class DreamSerializer(ModelSerializer):
    class MoneyField(serializers.Field):
        def to_representation(self, obj):
            return {
                'amount': "%f" % (obj.amount),
                'currency': "%s" % (obj.currency),
            }

        def to_internal_value(self, data):
            return Money(data['amount'], data['currency'])

    budget = MoneyField()

    class Meta:
        model = Dream
        # fields = ['id', 'title', 'description']
        fields = '__all__'
