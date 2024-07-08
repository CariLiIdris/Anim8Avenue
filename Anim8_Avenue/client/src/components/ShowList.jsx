import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getAllShows } from '../services/showService';

function ShowList() {
  const [shows, setShows] = useState([]);

  useEffect(() => {
    const fetchShows = async () => {
      try {
        const response = await getAllShows();
        setShows(response);
      } catch (error) {
        console.error(error);
      }
    };
    fetchShows();
  }, []);

  return (
    <div>
      <h1>Show List</h1>
      <ul>
        {shows.map((show) => (
          <li key={show._id}>
            <Link to={`/shows/${show._id}`}>{show.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ShowList;