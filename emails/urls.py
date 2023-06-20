from django.urls import path

from cardman.settings import SNS_ENDPOINT_SECRET
from .views import *

urlpatterns = [
    # get path from environment variable SECURE_URL
    path('inbound/' + SNS_ENDPOINT_SECRET + '/', InboundEmailView.as_view(), name='email-view'),
]
