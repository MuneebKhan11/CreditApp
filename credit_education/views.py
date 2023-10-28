from django.http import HttpResponse
from rest_framework import generics
from .models import UserCreditInfo
from .serializers import UserCreditInfoSerializer
def home(request):
    return HttpResponse("Hello!! Capital One, Credit Education!")


class UserCreditInfoListCreate(generics.ListCreateAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer
