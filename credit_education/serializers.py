from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserCreditInfo, CreditTransaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserCreditInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreditInfo
        fields = '__all__'


class CreditTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditTransaction
        fields = '__all__'


