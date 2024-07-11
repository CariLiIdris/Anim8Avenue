import React from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

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
  );
}

export default CategoriesPage;