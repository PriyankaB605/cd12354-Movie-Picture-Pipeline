import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MovieDetail({ movie }) {
  const [details, setDetails] = useState(null);
  const [error, setError] = useState(null);
  useEffect(() => {
    setDetails(null);
    setError(null);
    axios
      .get(`${process.env.REACT_APP_MOVIE_API_URL}/movies/${movie.id}`)
      .then((response) => setDetails(response.data))
      .catch(() => setError('Unable to load movie details.'));
  }, [movie]);

  if (error) return <p role="alert">{error}</p>;

  return (
    <div>
      {details && <h2>{details.movie.title}</h2>}
      {details && <p>{details.movie.description}</p>}
    </div>
  );
}

export default MovieDetail;
