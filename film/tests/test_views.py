import pytest

from film.models import Film
from producer.models import Producer


@pytest.mark.django_db
class TestFilmViews:
    def test_create_film(self, client) -> None:
        assert Film.objects.count() == 0
        producer: Producer = Producer.objects.create(name="Ben", email="ben@gmail.com")
        response = client.post(
            "/films/",
            {"title": "Harry Potter", "year_published": 2000, "producer": producer.id},
        )
        assert response.status_code == 201, response.data
        assert Film.objects.count() == 1

    def test_list_films(self, client) -> None:
        assert Film.objects.count() == 0
        producer = Producer.objects.create(name="Ben", email="ben@gmail.com")
        film = Film.objects.create(
            title="The Godfather", year_published=1972, producer=producer
        )

        response = client.get("/films/")

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": film.id,
                "producer": 1,
                "title": "The Godfather",
                "year_published": 1972,
            }
        ]

    def test_get_film_detail(self, client) -> None:
        producer = Producer.objects.create(name="Ben", email="ben@gmail.com")
        film = Film.objects.create(
            title="The Godfather", year_published=1972, producer=producer
        )

        response = client.get(f"/films/{film.id}/")

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "producer": {"email": "ben@gmail.com", "id": 1, "name": "Ben"},
            "title": "The Godfather",
            "year_published": 1972,
        }
