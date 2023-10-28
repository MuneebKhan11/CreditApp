from rest_framework import serializers
from .models import UserCreditInfo

class UserCreditInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreditInfo
        fields = '__all__'
