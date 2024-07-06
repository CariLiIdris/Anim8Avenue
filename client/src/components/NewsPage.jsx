import React from 'react';
import axios from 'axios';

function NewsPage() {
  const [news, setNews] = React.useState([]);

  React.useEffect(() => {
    axios.get('https://anime-api.com/api/news')
      .then(response => {
        setNews(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>News Page</h1>
      <ul>
        {news.map(item => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default NewsPage;