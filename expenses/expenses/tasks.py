from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_expense_notification(email, total_amount):
    subject = 'Expense Notification'
    message = f'You have been added to an expense. Total amount owed: {total_amount}.'
    from_email = 'email@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

@shared_task
def send_weekly_email():
    # Your logic to calculate total amount owed to each user
    # Example: total_amount_owed = calculate_total_amount_owed()

    subject = 'Weekly Expense Reminder'
    message = f'Total amount owed: {total_amount_owed}.'
    from_email = 'email@example.com'
    
    # Get all users or specific users you want to notify
    users = User.objects.all()

    for user in users:
        send_mail(subject, message, from_email, [user.email], fail_silently=False)