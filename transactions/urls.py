from django.urls import path

from .views import *

urlpatterns = [
    path('card/<int:card_id>/', CardTransactionListView.as_view(), name='card-transactions-list-view'),
    path('add/', AddTransactionView.as_view(), name='add-transactions-view'),
    path('', AllTransactionListView.as_view(), name='transactions-list-view'),
]
