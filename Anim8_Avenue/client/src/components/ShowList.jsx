/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getAllShows } from '../services/showService';

function ShowList() {
  const [shows, setShows] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    getAllShows()
      .then((res) => {
        setShows(res);
      })
      .catch((error) => {
        console.error('Failed to fetch shows:', error);
      });
  }, []);

  return (
    <div className="show-list-container">
      <h1>Show List</h1>
      <button className="add-show-button" onClick={() => navigate('/shows/create')}>Add Show</button>
      <ul className="show-list">
        {shows.map((show) => (
          <li key={show._id} className="show-item">
            <Link to={`/shows/${show._id}`} className="show-link">
              <div className="show-card">
                <h2>{show.name} - <span>{show.category}</span></h2>
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ShowList;