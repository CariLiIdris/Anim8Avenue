/* eslint-disable no-unused-vars */


import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <h1 className='head'><Link to={'/'}>Anim8Ave</Link></h1>
    </header>
  );
}

export default Header;