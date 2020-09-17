from instapic.models import Instapic
from .serializers import InstapicSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class InstapicViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Instapic.objects.all()
        serializer = InstapicSerializer(queryset, many=True)
        return Response(serializer.data)