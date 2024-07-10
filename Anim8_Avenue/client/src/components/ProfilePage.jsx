import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import axios from 'axios';

const ProfilePage = () => {
  const [user, setUser] = useState({});
  const [shows, setShows] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
    } else {
      axios.get('/api/user', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
     .then(response => {
        setUser(response.data);
        axios.get('/api/shows', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
       .then(response => {
          setShows(response.data);
        })
       .catch(error => {
          console.error(error);
        });
      })
     .catch(error => {
        console.error(error);
      });
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="profile-page">
      <h1>Profile Page</h1>
      <p>Welcome, {user.username}!</p>
      <p>Email: {user.email}</p>
      <h2>Personalized Shows:</h2>
      <ul>
        {shows.map(show => (
          <li key={show.id}>{show.name}</li>
        ))}
      </ul>
      <button onClick={handleLogout}>Log Out</button>
    </div>
  );
};

export default ProfilePage;
