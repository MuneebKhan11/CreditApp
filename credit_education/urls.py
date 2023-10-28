from django.urls import path
from . import views

urlpatterns = [
    path('api/usercreditinfo/', views.UserCreditInfoList.as_view(), name='usercreditinfo-list-create'),
    path('api/usercreditinfo/<int:pk>/', views.UserCreditInfoDetail.as_view(), name='usercreditinfo-detail'),
    path('api/users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('api/transactions/', views.CreditTransactionListCreate.as_view(), name='transaction-list-create'),
]
