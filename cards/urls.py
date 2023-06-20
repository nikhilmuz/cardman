from django.urls import path

from .views import *

urlpatterns = [
    path('add/', CardAddView.as_view(), name='card-add-view'),
    path('', CardListView.as_view(), name='card-list-view'),
]
