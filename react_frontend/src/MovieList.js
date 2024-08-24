import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './App.css'; // Importing CSS for styling

function MovieList() {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/movies/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setMovies(data))
      .catch(error => {
        console.error('Error fetching movies:', error);
        setError(error.message);
      });
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="App">
      <h2>Movie List</h2>
      <ul>
        {movies.map(movie => (
          <li key={movie.id}>
            <Link to={`/movies/${movie.id}`}>{movie.title} ({movie.year})</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MovieList;