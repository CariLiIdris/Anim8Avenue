/* eslint-disable no-unused-vars */
// Zacarias

import React from 'react';
import axios from 'axios';

function NewsPage() {
  const [news, setNews] = React.useState([]);

  React.useEffect(() => {
    axios.get('https://api.jikan.moe/v4/top/anime')
      .then(response => {
        // Limit to top 9 items
        setNews(response.data.data.slice(0, 9));
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div className="news-page-container">
      <h1>Anime News</h1>
      <div className="news-list">
        {news.map(item => (
          <div key={item.mal_id} className="news-item">
            <h2>{item.title}</h2>
            <img src={item.images.jpg.image_url} alt={item.title} className="news-image" />
            <p className="news-synopsis">{item.synopsis}</p>
            <p className="news-details">
              <strong>Aired:</strong> {item.aired.string} <br />
              <strong>Episodes:</strong> {item.episodes} <br />
              <strong>Rating:</strong> {item.rating} <br />
              <strong>Score:</strong> {item.score} ({item.scored_by} users)
            </p>
            <a href={`https://myanimelist.net/anime/${item.mal_id}`} target="_blank" rel="noopener noreferrer">Read more</a>
            {item.trailer && (
              <div className="trailer">
                <a href={item.trailer.url} target="_blank" rel="noopener noreferrer">Watch Trailer</a>
                <iframe
                  title="Trailer"
                  width="300"
                  height="200"
                  src={`https://www.youtube.com/embed/${item.trailer.youtube_id}`}
                  frameBorder="0"
                  allow="accelerometer; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default NewsPage;