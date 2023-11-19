from django.core.serializers import serialize
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import UserProfile, Expense, Transaction

def serialize_model(model):
    return serialize('json', [model], use_natural_primary_keys=True)[1:-1]

def json_response(data):
    return JsonResponse(data, safe=False)

def serialize_user_profile(user_profile):
    return model_to_dict(user_profile.user)

def serialize_expense(expense):
    serialized_expense = model_to_dict(expense)
    serialized_expense['created_by'] = serialize_user_profile(expense.created_by)
    serialized_expense['participants'] = [serialize_user_profile(user) for user in expense.participants.all()]
    serialized_expense['transactions'] = [serialize_model(transaction) for transaction in expense.transactions.all()]
    return serialized_expense

def serialize_transaction(transaction):
    serialized_transaction = model_to_dict(transaction)
    serialized_transaction['payer'] = serialize_user_profile(transaction.payer)
    serialized_transaction['payee'] = serialize_user_profile(transaction.payee)
    return serialized_transaction
