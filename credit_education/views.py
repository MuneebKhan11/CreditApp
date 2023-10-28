from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserCreditInfo
from .serializers import UserCreditInfoSerializer
from django.contrib.auth.models import User
class UserCreditInfoList(generics.ListCreateAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer

class UserCreditInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer



class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreditTransactionListCreate(generics.ListCreateAPIView):
    queryset = CreditTransaction.objects.all()
    serializer_class = CreditTransactionSerializer

def home(request):
    return HttpResponse("Hello!! Capital One, Credit Education!")