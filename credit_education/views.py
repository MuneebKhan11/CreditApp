from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserCreditInfo
from .serializers import UserCreditInfoSerializer

class UserCreditInfoList(generics.ListCreateAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer

class UserCreditInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer


def home(request):
    return HttpResponse("Hello!! Capital One, Credit Education!")