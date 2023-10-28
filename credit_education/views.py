from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import UserCreditInfo, CreditTransaction, Account
from django.contrib.auth.models import User
from .serializers import UserCreditInfoSerializer, UserSerializer, CreditTransactionSerializer
from .api_utils import create_random_account
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
import json
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {"user": request.user})


def home(request):
    return render(request, 'index.html')


class UserCreditInfoList(generics.ListCreateAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer


class UserCreditInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCreditInfo.objects.all()
    serializer_class = UserCreditInfoSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


def fetch_accounts(request):
    try:
        new_account_data = create_random_account(quantity=2, num_transactions=5, live_balance=True)
        accounts_data = new_account_data.get('Accounts', [])

        for account in accounts_data:
            live_balance_json = json.loads(account['liveBalance'])
            live_balance_value = live_balance_json.get('status', False)  # Defaults to False if 'status' is not present

            Account.objects.create(
                firstname=account['firstname'],
                lastname=account['lastname'],
                creditScore=account['creditScore'],
                liveBalance=live_balance_value,  # Use the parsed boolean value here
                accountId=account['accountId'],
                phoneNumber=account['phoneNumber'],
                balance=account['balance'],
                creditLimit=account['creditLimit'],
                uci=account['uci'],
                riskScore=account['riskScore'],
                state=account['state'],
                currencyCode=account['currencyCode'],
                email=account['email'],
                productType=account['productType'],
                homeAddress=account['homeAddress'],
            )
        return JsonResponse({"status": "Accounts fetched and saved successfully!"})
    except Exception as e:
        return JsonResponse({"status": f"Error: {str(e)}"}, status=500)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


