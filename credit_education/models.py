from django.db import models

class UserCreditInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    income = models.FloatField()
    current_credit_score = models.PositiveIntegerField()
    target_credit_score = models.PositiveIntegerField()
    education_material_viewed = models.PositiveIntegerField(default=0)  # Number of educational resources viewed

    def __str__(self):
        return self.name
