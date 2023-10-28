from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/usercreditinfo/', views.UserCreditInfoListCreate.as_view(), name='usercreditinfo-list-create'),
]
