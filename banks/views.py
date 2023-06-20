from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *


class BankListView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
