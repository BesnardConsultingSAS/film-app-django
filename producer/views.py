from rest_framework import viewsets

from producer.models import Producer
from producer.serializers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
