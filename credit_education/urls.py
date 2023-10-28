from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('api/usercreditinfo/', views.UserCreditInfoListCreate.as_view(), name='usercreditinfo-list-create'),
    path('api/credittransactions/', views.CreditTransactionList.as_view(), name='credittransaction-list'),
    path('api/credittransactions/<int:pk>/', views.CreditTransactionDetail.as_view(), name='credittransaction-detail'),
    path('fetch-accounts/', views.fetch_accounts, name='fetch_accounts'),
    # path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('accounts/', include('allauth.urls')),

]
