/* eslint-disable no-unused-vars */
import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createUser } from '../services/userService.jsx';
import { userContext } from '../context/userContext.jsx';

function RegisterPage() {
  const navigate = useNavigate();
  const { setUser, storeIdInLocalStorage } = useContext(userContext);

  // Both
  const [userData, setUserData] = useState({
    username: '',
    fName: '',
    lName: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [errors, setErrors] = useState({
    username: '',
    fname: '',
    lname: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [registered, setRegistered] = useState(false);

  // Nehimya
  const handleFormChange = e => {
    const { name, value } = e.target;

    // Validate the field as you type
    let error = '';
    if (name === 'username') {
      if (value.length < 3) {
        error = 'Username must be at least 3 characters';
      }
    } else if (name === 'fName' || name === 'lName') {
      if (value.length < 2) {
        error = 'Name must be at least 2 characters';
      }
    } else if (name === 'email') {
      if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(value)) {
        error = 'Invalid email address';
      }
    } else if (name === 'password') {
      if (value.length < 8) {
        error = 'Password must be at least 8 characters';
      }
    } else if (name === 'confirmPassword') {
      if (value !== userData.password) {
        error = 'Passwords do not match';
      }
    }

    setErrors((prevErrors) => ({ ...prevErrors, [name]: error }));
    setUserData((prevForm) => ({ ...prevForm, [name]: value }));
  };

  // Zacarias
  const handleSubmit = async e => {
    e.preventDefault();

    createUser(userData)
      .then(res => {
        setUser(res.User);
        // Nehimya
        setRegistered(true);
        // Zacarias
        storeIdInLocalStorage(res.userID);
      })
      .catch(error => {
        setErrors(error.response?.data.errors);
      });
  };

  if (registered) {
    navigate('/profile', { replace: true });
  }

  return (
    <div className="register-container">
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <label>Username:</label>
        <input type="text" name="username" value={userData.username} onChange={handleFormChange} />
        {errors?.username && <span className="error">{errors.username}</span>}
        <br />
        <label>First Name:</label>
        <input type="text" name="fName" value={userData.fName} onChange={handleFormChange} />
        {errors?.fname && <span className="error">{errors?.fname}</span>}
        <br />
        <label>Last Name:</label>
        <input type="text" name="lName" value={userData.lName} onChange={handleFormChange} />
        {errors?.lname && <span className="error">{errors?.lname}</span>}
        <br />
        <label>Email:</label>
        <input type="email" name="email" value={userData.email} onChange={handleFormChange} />
        {errors?.email && <span className="error">{errors?.email}</span>}
        <br />
        <label>Password:</label>
        <input type="password" name="password" value={userData.password} onChange={handleFormChange} />
        {errors?.password && <span className="error">{errors?.password}</span>}
        <br />
        <label>Confirm Password:</label>
        <input type="password" name="confirmPassword" value={userData.confirmPassword} onChange={handleFormChange} />
        {errors?.confirmPassword && <span className="error">{errors?.confirmPassword}</span>}
        <br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default RegisterPage;