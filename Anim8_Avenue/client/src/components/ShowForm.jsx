/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { createShow } from '../services/showService';
import { useNavigate } from 'react-router-dom';

const categories = [
  "Slice of life",
  "Shonen",
  "Isekai",
  "Josei",
  "Shoujo",
  "Comedy",
  "Mecha",
  "Adventure fiction",
  "Fantasy",
  "Seinen",
  "Action",
  "Romance",
  "Sci-fi",
  "Harem",
  "Drama",
  "Horror",
  "Supernatural fiction",
  "Historical",
  "Children's anime and manga",
  "Mystery",
  "Psychology",
  "Demons",
  "Ecchi",
  "Action anime"
];

function ShowForm() {
  const [showData, setShowData] = useState({
    name: '',
    description: '',
    category: '',
    image: null
  });
  const [errors, setErrors] = useState({
    name: '',
    description: '',
    category: '',
    image: ''
  });

  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;

    // Validate the field as you type
    let error = '';
    if (name === 'name') {
      if (value.length < 3) {
        error = 'Name must be at least 3 characters';
      }
    } else if (name === 'description') {
      if (value.length < 10) {
        error = 'Description must be at least 10 characters';
      }
    }

    setErrors((prevErrors) => ({ ...prevErrors, [name]: error }));
    setShowData((prevForm) => ({ ...prevForm, [name]: value }));
  };

  const handleFileChange = (e) => {
    setShowData((prevForm) => ({ ...prevForm, image: e.target.files[0] }));
  };

  const handleCategoryChange = (e) => {
    setShowData((prevForm) => ({ ...prevForm, category: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await createShow(showData);
      // console.log(showData)
      window.alert('Show created successfully!');
      navigate('/shows');
    } catch (error) {
      setErrors((prevErrors) => ({ ...prevErrors, form: 'Failed to create show' }));
      window.alert('Failed to create show');
    }
  };

  return (
    <div className="show-form-container">
      <h1>Create Show</h1>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={showData.name}
          onChange={handleInputChange}
        />
        {errors.name && <span style={{ color: 'red' }}>{errors.name}</span>}
        <br />
        <label>Description:</label>
        <textarea
          name="description"
          value={showData.description}
          onChange={handleInputChange}
        />
        {errors.description && <span style={{ color: 'red' }}>{errors.description}</span>}
        <br />
        <label>Category:</label>
        <select name="category" value={showData.category} onChange={handleCategoryChange}>
          <option value="">Select a category</option>
          {categories.map(category => (
            <option key={category} value={category}>{category}</option>
          ))}
        </select>
        {errors.category && <span style={{ color: 'red' }}>{errors.category}</span>}
        <br />
        <label>Image:</label>
        <input
          type="file"
          name="image_url"
          onChange={handleFileChange}
        />
        {errors.image && <span style={{ color: 'red' }}>{errors.image}</span>}
        <br />
        <button type="submit">Create Show</button>
        {errors.form && <div style={{ color: 'red' }}>{errors.form}</div>}
      </form>
    </div>
  );
}

export default ShowForm;