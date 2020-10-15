from rest_framework import serializers

from film.models import Film
from producer.serializers import ProducerSerializer


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class FilmDetailSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(read_only=True)

    class Meta:
        model = Film
        fields = "__all__"
