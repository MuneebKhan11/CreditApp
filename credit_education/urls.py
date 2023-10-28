from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/usercreditinfo/', views.UserCreditInfoListCreate.as_view(), name='usercreditinfo-list-create'),
    path('api/credittransactions/', views.CreditTransactionList.as_view(), name='credittransaction-list'),
    path('api/credittransactions/<int:pk>/', views.CreditTransactionDetail.as_view(), name='credittransaction-detail'),
]
