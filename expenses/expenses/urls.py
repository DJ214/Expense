"""
URL configuration for expenses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
## from django.contrib import admin
from django.urls import path
from . import views
from .views import create_expense, get_expense,get_user_profile,get_user_balances,simplify_expenses

urlpatterns = [
    path('user-profile/', get_user_profile, name='get_user_profile'),
    path('create-expense/', create_expense, name='create_expense'),
    path('get-expense/<int:expense_id>/', get_expense, name='get_expense'),
    path('get-user-balances/', get_user_balances, name='get_user_balances'),
    path('simplify-expenses/', simplify_expenses, name='simplify_expenses'),
]
