from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)

class Expense(models.Model):
    EQUAL = 'EQUAL'
    EXACT = 'EXACT'
    PERCENT = 'PERCENT'

    EXPENSE_TYPE_CHOICES = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENT, 'Percent'),
    ]

    name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_expenses')
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPE_CHOICES)
    expense_date = models.DateField()
    is_simplified = models.BooleanField(default=False)

class Transaction(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='transactions')
    payer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='transactions_as_payer')
    payee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='transactions_as_payee')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
