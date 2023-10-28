from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import UserCreditInfo, CreditTransaction
from django.contrib.auth.models import User
from .serializers import UserCreditInfoSerializer, UserSerializer, CreditTransactionSerializer


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


class UserCreditInfoListCreate(generics.ListCreateAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer


class CreditTransactionList(generics.ListCreateAPIView):
    queryset = CreditTransaction.objects.all()
    serializer_class = CreditTransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return CreditTransaction.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreditTransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditTransaction.objects.all()
    serializer_class = CreditTransactionSerializer

    def get_object(self):
        obj = get_object_or_404(CreditTransaction, pk=self.kwargs["pk"], user=self.request.user)
        return obj


def home(request):
    return HttpResponse("Hello!! Capital One, Credit Education!")
