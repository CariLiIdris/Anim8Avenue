/* eslint-disable no-unused-vars */
// LoginForm.js
import React, { useContext, useState } from 'react';
import { login } from '../services/userService';
import { userContext } from '../context/userContext';
import { useNavigate } from 'react-router-dom';

function LoginForm() {
  const [form, setForm] = useState({ username: '', password: '' });
  const [errors, setErrors] = useState({ username: '', password: '' });
  const { setUser, storeIdInLocalStorage } = useContext(userContext)
  const navigate = useNavigate();

  const handleFormChange = (event) => {
    const { name, value } = event.target;
    setForm((prevForm) => ({ ...prevForm, [name]: value }));

    validateField(name, value);
  };

  const validateField = (name, value) => {
    switch (name) {
      case 'username':
        if (!value) {
          setErrors((prevErrors) => ({ ...prevErrors, username: 'Username is required' }));
        } else {
          setErrors((prevErrors) => ({ ...prevErrors, username: '' }));
        }
        break;
      case 'password':
        if (!value) {
          setErrors((prevErrors) => ({ ...prevErrors, password: 'Password is required' }));
        } else if (value.length < 8) {
          setErrors((prevErrors) => ({ ...prevErrors, password: 'Password must be at least 8 characters' }));
        } else {
          setErrors((prevErrors) => ({ ...prevErrors, password: '' }));
        }
        break;
      default:
        break;
    }
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    if (Object.keys(errors).every((key) => errors[key] === '')) {
      // Login logic here
      login(form)
        .then((res) => {
          // console.log(res)
          setUser(res.user)
          storeIdInLocalStorage(res.user._id)
          navigate('/')
        })
      // You can call an API or perform any other login logic here
      console.log('Login successful!');
    }
  };

  return (
    <form className="login-form" onSubmit={handleFormSubmit}>
      <h1>Login</h1>
      <label>Username:</label>
      <input type='text' name="username" value={form.username} onChange={handleFormChange} />
      {errors.username && <div className="error">{errors.username}</div>}
      <br />
      <label>Password:</label>
      <input type="password" name="password" value={form.password} onChange={handleFormChange} />
      {errors.password && <div className="error">{errors.password}</div>}
      <br />
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;
