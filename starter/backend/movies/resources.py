from flask import jsonify, request
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            # Return a list of all movies
            return jsonify({"movies": [dict(movie, id=int(movie_id)) for movie_id, movie in movies.items()]})

        movie = movies.get(str(movie_id))
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404
        return jsonify({"movie": dict(movie, id=movie_id)})

    def post(self):
        movie = request.get_json(silent=True) or {}
        if not movie.get("title") or not movie.get("description"):
            return jsonify({"error": "title and description are required"}), 400

        movie_id = str(max((int(movie_id) for movie_id in movies), default=0) + 1)
        movies[movie_id] = {"title": movie["title"], "description": movie["description"]}
        return jsonify({"movie": dict(movies[movie_id], id=int(movie_id))}), 201

    def put(self, movie_id):
        movie = movies.get(str(movie_id))
        if movie is None:
            return jsonify({"error": "Movie not found"}), 404

        updates = request.get_json(silent=True) or {}
        movie.update({field: updates[field] for field in ("title", "description") if field in updates})
        if not movie.get("title") or not movie.get("description"):
            return jsonify({"error": "title and description are required"}), 400
        return jsonify({"movie": dict(movie, id=movie_id)})

    def delete(self, movie_id):
        if movies.pop(str(movie_id), None) is None:
            return jsonify({"error": "Movie not found"}), 404
        return "", 204
