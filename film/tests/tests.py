import pytest

from film.models import Film


@pytest.mark.django_db
class TestFilmViews:
    def test_create_film(self, client) -> None:
        assert Film.objects.count() == 0
        response = client.post(
            "/films/",
            {
                "title": "Harry Potter",
                "year_published": 2000
            }
        )
        assert response.status_code == 201, response.data
        assert Film.objects.count() == 1

    def test_list_films(self, client) -> None:
        assert Film.objects.count() == 0
        film = Film.objects.create(
            title="The Godfather",
            year_published=1972
        )

        response = client.get(
            "/films/"
        )

        assert response.status_code == 200
        assert response.json() == [{
            "id": film.id,
            "title": "The Godfather",
            "year_published": 1972
        }]
