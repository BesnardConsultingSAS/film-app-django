from django.db import models

from producer.models import Producer


class Film(models.Model):
    title = models.CharField(max_length=100)
    year_published = models.PositiveSmallIntegerField(null=False)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
