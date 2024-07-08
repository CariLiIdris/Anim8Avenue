import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // initialize isLoggedIn to false

  return (
    <nav>
      <ul>
        <li><Link to="/">Trending</Link></li>
        <li><Link to="/news">News</Link></li>
        <li><Link to="/categories">Categories</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/register">Register</Link></li>
      </ul>
      <div className="dropdown">
        {isLoggedIn ? (
          <li><Link to="/profile">Account</Link></li>
        ) : (
          <li><Link to="/login">Login</Link></li>
        )}
        <Link to="/register">Register</Link>
      </div>
    </nav>
  );
}

export default Navigation;