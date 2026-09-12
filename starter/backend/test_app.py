from . import app
import os


def test_movies_endpoint_returns_200():
    with app.test_client() as client:
        status_code = os.getenv("FAIL_TEST", 200)
        response = client.get("/movies/")
        assert response.status_code == status_code


def test_movies_endpoint_returns_json():
    with app.test_client() as client:
        response = client.get("/movies/")
        assert response.content_type == "application/json"


def test_movies_endpoint_returns_valid_data():
    with app.test_client() as client:
        response = client.get("/movies/")
        data = response.get_json()
        assert isinstance(data, dict)
        assert "movies" in data
        assert isinstance(data.get("movies"), list)
        assert len(data["movies"]) > 0
        assert "title" in data["movies"][0]


def test_movie_crud_routes():
    with app.test_client() as client:
        created = client.post(
            "/movies", json={"title": "Test Movie", "description": "Test"}
        )
        assert created.status_code == 201
        movie_id = created.get_json()["movie"]["id"]

        updated = client.put(f"/movies/{movie_id}", json={"title": "Updated Movie"})
        assert updated.status_code == 200
        assert updated.get_json()["movie"]["title"] == "Updated Movie"

        deleted = client.delete(f"/movies/{movie_id}")
        assert deleted.status_code == 204
        assert client.get(f"/movies/{movie_id}").status_code == 404
