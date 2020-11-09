import pytest

from film.models import Film
from film.tests.film_factory import FilmFactory
from producer.models import Producer
from producer.tests.producer_factory import ProducerFactory


@pytest.mark.django_db
class TestFilmViews:
    def test_create_film(self, client) -> None:
        assert Film.objects.count() == 0
        producer: Producer = ProducerFactory()
        response = client.post(
            "/films/",
            {"title": "Harry Potter", "year_published": 2000, "producer": producer.id},
        )
        assert response.status_code == 201, response.data
        assert Film.objects.count() == 1

    def test_list_films(self, client) -> None:
        assert Film.objects.count() == 0
        film: Film = FilmFactory()

        response = client.get("/films/")

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": film.id,
                "producer": film.producer.id,
                "title": film.title,
                "year_published": film.year_published,
            }
        ]

    def test_get_film_detail(self, client) -> None:
        film: Film = FilmFactory()

        response = client.get(f"/films/{film.id}/")

        assert response.status_code == 200
        assert response.json() == {
            "id": film.id,
            "producer": {
                "id": film.producer.id,
                "email": film.producer.email,
                "name": film.producer.name,
            },
            "title": film.title,
            "year_published": film.year_published,
        }
