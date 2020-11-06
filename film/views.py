from rest_framework import viewsets

from film.models import Film
from film.serializers import FilmSerializer, FilmDetailSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return FilmDetailSerializer
        return FilmSerializer
