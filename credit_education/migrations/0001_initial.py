# Generated by Django 4.2.6 on 2023-10-28 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('creditScore', models.IntegerField()),
                ('liveBalance', models.BooleanField()),
                ('accountId', models.CharField(max_length=50, unique=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creditLimit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uci', models.CharField(max_length=50)),
                ('riskScore', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('currencyCode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('productType', models.CharField(max_length=20)),
                ('homeAddress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCreditInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('income', models.FloatField()),
                ('current_credit_score', models.PositiveIntegerField()),
                ('target_credit_score', models.PositiveIntegerField()),
                ('education_material_viewed', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], default='DEBIT', max_length=6)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
