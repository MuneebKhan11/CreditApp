from django.db import models
from django.contrib.auth.models import User


class UserCreditInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    income = models.FloatField()
    current_credit_score = models.PositiveIntegerField()
    target_credit_score = models.PositiveIntegerField()
    education_material_viewed = models.PositiveIntegerField(default=0)  # Number of educational resources viewed

    from django.contrib.auth.models import User


class CreditTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TRANSACTION_TYPES = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    ]
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES, default='DEBIT')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        user_credit_info = self.user.usercreditinfo
        if self.transaction_type == "DEBIT":
            user_credit_info.current_credit_score -= self.amount
        else:
            user_credit_info.current_credit_score += self.amount
        user_credit_info.save()


class Account(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    creditScore = models.IntegerField()
    liveBalance = models.BooleanField()
    accountId = models.CharField(max_length=50, unique=True)
    phoneNumber = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    creditLimit = models.DecimalField(max_digits=10, decimal_places=2)
    uci = models.CharField(max_length=50)
    riskScore = models.IntegerField()
    state = models.CharField(max_length=20)
    currencyCode = models.CharField(max_length=10)
    email = models.EmailField()
    productType = models.CharField(max_length=20)
    homeAddress = models.TextField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_score = models.IntegerField(default=0)


def __str__(self):
    return self.name
