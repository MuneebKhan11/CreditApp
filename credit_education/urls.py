from django.urls import path
from . import views

urlpatterns = [
    path('api/usercreditinfo/', views.UserCreditInfoList.as_view(), name='usercreditinfo-list-create'),
    path('api/usercreditinfo/<int:pk>/', views.UserCreditInfoDetail.as_view(), name='usercreditinfo-detail'),
]
