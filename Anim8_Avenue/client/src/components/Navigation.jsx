/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
import React, { useContext, useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { userContext } from '../context/userContext';
import Cookies from 'js-cookie'

function Navigation({ submitFunction }) {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // initialize isLoggedIn to false
  const { user } = useContext(userContext)
  const navigate = useNavigate();

  useEffect(() => {
    if (user._id) {
      setIsLoggedIn(true)
    }
  }, [user._id])

  const handleLogout = () => {
    submitFunction()
      .then(() => {
        Cookies.remove('userToken')
        setIsLoggedIn(false)
        window.localStorage.removeItem('Logged in user id')
        navigate('/login')
      })
  }

  return (
    <nav>
      <ul>
        <li><Link to="/">Trending</Link></li>
        <li><Link to="/news">News</Link></li>
        <li><Link to="/categories">Categories</Link></li>
      </ul>
      <div className="dropdown">
        {isLoggedIn ? (
          <>
            <li><Link to="/profile">Account</Link></li>
            <button className='navLink logoutBttn' onClick={handleLogout}>
              Logout
            </button>
          </>
        ) : (
          <>
            <li><Link to="/login">Login</Link></li>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navigation;