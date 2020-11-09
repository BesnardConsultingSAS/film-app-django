import factory
from factory.django import DjangoModelFactory

from producer.models import Producer


class ProducerFactory(DjangoModelFactory):
    class Meta:
        model = Producer

    name = factory.Faker("first_name")
    email = factory.LazyAttribute(lambda obj: "%s@example.com" % obj.name)
