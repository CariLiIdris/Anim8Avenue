/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createUser } from '../services/userService.jsx';

function RegisterPage() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
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

  const handleFormChange = (event) => {
    const { name, value } = event.target;

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
      if (value !== form.password) {
        error = 'Passwords do not match';
      }
    }

    setErrors((prevErrors) => ({ ...prevErrors, [name]: error }));

    setForm((prevForm) => ({ ...prevForm, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const { username, fName, lName, email, password, confirmPassword } = form;

    const newUser = {
      username,
      fName,
      lName,
      email,
      password,
    };

    try {
      const response = await createUser(newUser);
      setRegistered(true);
    } catch (error) {
      setErrors(error.response.data.errors);
    }
  };

  if (registered) {
    navigate('/profile', { replace: true });
  }

  return (
    <div>
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <label>Username:</label>
        <input type="text" name="username" value={form.username} onChange={handleFormChange} />
        {errors.username && <span style={{ color: 'red' }}>{errors.username}</span>}
        <br />
        <label>First Name:</label>
        <input type="text" name="fName" value={form.fName} onChange={handleFormChange} />
        {errors.fname && <span style={{ color: 'red' }}>{errors.fname}</span>}
        <br />
        <label>Last Name:</label>
        <input type="text" name="lName" value={form.lName} onChange={handleFormChange} />
        {errors.lname && <span style={{ color: 'red' }}>{errors.lname}</span>}
        <br />
        <label>Email:</label>
        <input type="email" name="email" value={form.email} onChange={handleFormChange} />
        {errors.email && <span style={{ color: 'red' }}>{errors.email}</span>}
        <br />
        <label>Password:</label>
        <input type="password" name="password" value={form.password} onChange={handleFormChange} />
        {errors.password && <span style={{ color: 'red' }}>{errors.password}</span>}
        <br />
        <label>Confirm Password:</label>
        <input type="password" name="confirmPassword" value={form.confirmPassword} onChange={handleFormChange} />
        {errors.confirmPassword && <span style={{ color: 'red' }}>{errors.confirmPassword}</span>}
        <br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default RegisterPage;