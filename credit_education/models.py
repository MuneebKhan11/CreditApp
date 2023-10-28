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
        if self.transaction_type == "DEBIT":
            self.user.usercreditinfo.credit_score -= self.amount
        else:
            self.user.usercreditinfo.credit_score += self.amount
            self.user.usercreditinfo.save()


def __str__(self):
    return self.name
