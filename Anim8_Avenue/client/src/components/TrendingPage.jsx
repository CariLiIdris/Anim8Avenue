/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function TrendingPage() {
  const [trendingShows, setTrendingShows] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/shows')
      .then(response => {
        // Assuming shows are sorted by popularity
        setTrendingShows(response.data.slice(0, 10));
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div className="trending-page">
      <h1>Trending Shows</h1>
      <div className="button-container">
        <Link to="/shows">
          <button className="nav-button">View All Shows</button>
        </Link>
        <Link to="/shows/create">
          <button className="nav-button">Add New Show</button>
        </Link>
      </div>
      <ul className="show-list">
        {trendingShows.map(show => (
          <li key={show._id} className="show-item">
            <h2>{show.name}</h2>
            <p>{show.description}</p>
            {show.image_url && (
              <img src={`http://localhost:8000/${show.image_url}`} alt={show.name} className="show-image" />
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TrendingPage;