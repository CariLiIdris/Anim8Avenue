import React from 'react';
import axios from 'axios';

function CategoriesPage() {
  const [categories, setCategories] = React.useState([]);

  React.useEffect(() => {
    axios.get('https://anime-api.com/api/categories')
      .then(response => {
        setCategories(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Categories Page</h1>
      <ul>
        {categories.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CategoriesPage;