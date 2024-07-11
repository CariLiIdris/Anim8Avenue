// Zacarias

import React from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Alb from '../assets/images/Albedoo.png'
import Luffy from '../assets/images/Luffy.png'
function CategoriesPage() {
  const [categories, setCategories] = React.useState([]);

  React.useEffect(() => {
    axios.get('http://localhost:8000/api/categories')
      .then(response => {
        setCategories(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    // Here
    <div className='CategoryImgGroup'>
      <img src={Alb} className='leftImg' alt="Albedo" />
      <div className="categories-page">
        <h1>Categories</h1>
        <ul>
          {categories.map((category, index) => (
            <li key={index}>
              <Link to={`/categories/${category}`}>{category}</Link>
            </li>
          ))}
        </ul>
      </div>
      <img src={Luffy} className='rightImg luffy' alt="Luffy" />
    </div>
    // Here
  );
}

export default CategoriesPage;