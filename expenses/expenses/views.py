from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Expense, Transaction
from .serializers import UserProfileSerializer, ExpenseSerializer, TransactionSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_expense(request):
    # Implement logic to create an expense based on request data
    # Make sure to handle different expense types (EQUAL, EXACT, PERCENT)
    # You may also want to send email notifications asynchronously
    return Response({"message": "Expense created successfully."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    serializer = ExpenseSerializer(expense)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_balances(request):
    # Implement logic to calculate and return user balances
    return Response({"message": "User balances retrieved successfully."})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def simplify_expenses(request):
    # Implement logic to simplify balances based on request data
    return Response({"message": "Expenses simplified successfully."})


from .tasks import send_expense_notification

# Your view function
def create_expense(request):
    # Your expense creation logic here

    # Trigger the task asynchronously
    for participant_email in participants_emails:
        send_expense_notification.delay(participant_email, total_amount)
    
    # Rest of view logic