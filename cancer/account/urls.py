from django.urls import path, include
from .views import account
urlpatterns = [
    path('account', account, name='account')
]

