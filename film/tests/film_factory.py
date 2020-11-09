import factory
from factory.django import DjangoModelFactory

from film.models import Film
from producer.tests.producer_factory import ProducerFactory


class FilmFactory(DjangoModelFactory):
    class Meta:
        model = Film

    title = factory.Sequence(lambda n: "Film %d" % n)
    year_published = 1992
    producer = factory.SubFactory(ProducerFactory)
