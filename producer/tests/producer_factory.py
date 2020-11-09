from factory.django import DjangoModelFactory

from producer.models import Producer


class ProducerFactory(DjangoModelFactory):
    class Meta:
        model = Producer

    name = "ben"
    email = "ben@example.com"
