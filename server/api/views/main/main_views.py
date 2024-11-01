from rest_framework import viewsets
from rest_framework.response import Response
from ...models import IncomeSource
from .serializer import IncomeSourceSerializer
from rest_framework.permissions import IsAuthenticated

class IncomeSourceView(viewsets.ModelViewSet):
    queryset = IncomeSource.objects.all()
    serializer_class = IncomeSourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IncomeSource.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)




