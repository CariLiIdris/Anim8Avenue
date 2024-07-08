// LoginForm.js
import React, { useState } from 'react';

function LoginForm() {
  const [form, setForm] = useState({ email: '', password: '' });
  const [errors, setErrors] = useState({ email: '', password: '' });

  const handleFormChange = (event) => {
    const { name, value } = event.target;
    setForm((prevForm) => ({ ...prevForm, [name]: value }));

    validateField(name, value);
  };

  const validateField = (name, value) => {
    switch (name) {
      case 'email':
        if (!value) {
          setErrors((prevErrors) => ({ ...prevErrors, email: 'Email is required' }));
        } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(value)) {
          setErrors((prevErrors) => ({ ...prevErrors, email: 'Invalid email address' }));
        } else {
          setErrors((prevErrors) => ({ ...prevErrors, email: '' }));
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
      // You can call an API or perform any other login logic here
      console.log('Login successful!');
    }
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <label>Email:</label>
      <input type="email" name="email" value={form.email} onChange={handleFormChange} />
      {errors.email && <div style={{ color: 'red' }}>{errors.email}</div>}
      <br />
      <label>Password:</label>
      <input type="password" name="password" value={form.password} onChange={handleFormChange} />
      {errors.password && <div style={{ color: 'red' }}>{errors.password}</div>}
      <br />
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;