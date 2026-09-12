import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

function MovieList({ onMovieClick }) {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_MOVIE_API_URL}/movies`)
      .then((response) => setMovies(response.data.movies))
      .catch(() => setError('Unable to load movies.'));
  }, []);

  if (error) return <p role="alert">{error}</p>;

  return (
    <ul>
      {movies.map((movie) => (
        <li className="movieItem" key={movie.id}>
          <button type="button" onClick={() => onMovieClick(movie)}>
            {movie.title}
          </button>
        </li>
      ))}
    </ul>
  );
}

MovieList.propTypes = {
  onMovieClick: PropTypes.func.isRequired,
};

export default MovieList;
