import React, { useState } from 'react';
import axios from 'axios';

function ShowForm() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/shows', { name, description })
      .then(response => {
        // Handle show creation success
      })
      .catch(error => {
        setError(error.response.data.error);
      });
  };

  return (
    <div>
      <h1>Create Show</h1>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        <br />
        <label>Description:</label>
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
        <br />
        <button type="submit">Create Show</button>
        {error && <div style={{ color: 'red' }}>{error}</div>}
      </form>
    </div>
  );
}

export default ShowForm;