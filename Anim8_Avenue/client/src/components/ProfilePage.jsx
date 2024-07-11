/* eslint-disable no-unused-vars */
import React, { useContext, useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { userContext } from '../context/userContext';
import { deleteUserById, logout, updateUserById } from '../services/userService';
import { useCookies } from 'react-cookie'

const ProfilePage = () => {
  // Zacarias
  const { user } = useContext(userContext);
  const [isEditing, setIsEditing] = useState(false);
  const [cookie, setCookie, removeCookie] = useCookies()
  // Nehimya
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    fName: '',
    lName: '',
    email: ''
  });

  useEffect(() => {
    const token = localStorage.getItem('Logged in user id');
    if (!token) {
      navigate('/login');
    } else if (user) {
      setFormData({
        username: user.username,
        fName: user.fName,
        lName: user.lName,
        email: user.email
      });
    }
  }, [user, navigate]);

  // Zacarias
  const handleLogout = () => {
    logout()
      .then(() => {
        navigate('/login');
      })
      .catch(error => { console.log(error) })
  };

  // Nehimya
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedUser = await updateUserById(user._id, formData);
      setIsEditing(false);
      window.location.reload();
    } catch (error) {
      console.error('Failed to update user', error);
    }
  };

  // Zacarias
  const handleDelete = async () => {
    try {
      await deleteUserById(user._id);
      localStorage.removeItem('Logged in user id');
      removeCookie('userToken', { path: '/', domain: 'localhost' });
      navigate('/');
    } catch (error) {
      console.error('Failed to delete user', error);
    }
  };

  return (
    <div className="profile-page">
      <h1>Profile Page</h1>
      {isEditing ? (
        <form onSubmit={handleFormSubmit}>
          <label>
            Username:
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
            />
          </label>
          <label>
            First Name:
            <input
              type="text"
              name="fName"
              value={formData.fName}
              onChange={handleInputChange}
            />
          </label>
          <label>
            Last Name:
            <input
              type="text"
              name="lName"
              value={formData.lName}
              onChange={handleInputChange}
            />
          </label>
          <label>
            Email:
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
            />
          </label>
          <button type="submit">Save Changes</button>
          <button type="button" onClick={() => setIsEditing(false)}>Cancel</button>
        </form>
      ) : (
        <>
          <p>Welcome 👋, {user.username}!</p>
          <p>First Name: {user.fName}</p>
          <p>Last Name: {user.lName}</p>
          <p>Email: {user.email}</p>
          <h2>Personalized Shows:</h2>
          <ul>
            {user.shows ? user.shows.map(show => (
              <li key={show._id}>{show.name}</li>
            )) : <p>No shows available</p>}
          </ul>
          <button onClick={() => setIsEditing(true)}>Edit Profile</button>
          <button onClick={handleDelete}>Delete Account</button>
        </>
      )}
    </div>
  );
};

export default ProfilePage;