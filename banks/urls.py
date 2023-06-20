from django.urls import path

from .views import *

urlpatterns = [
    path('', BankListView.as_view(), name='bank-list-view'),
]