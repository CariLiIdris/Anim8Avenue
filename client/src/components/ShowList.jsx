import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ShowList() {
  const [shows, setShows] = useState([]);

  useEffect(() => {
    axios.get('/api/shows')
      .then(response => {
        setShows(response.data);
      })
      .catch(error => {
        console.error(error);
      });
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