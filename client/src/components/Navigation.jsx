import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
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
        <button className="dropbtn">Account</button>
        <div className="dropdown-content">
          <Link to="/login">Login</Link>
          <Link to="/register">Register</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navigation;