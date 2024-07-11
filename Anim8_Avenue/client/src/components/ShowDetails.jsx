/* eslint-disable no-unused-vars */
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { getShowById, updateShowById, deleteShowById } from '../services/showService';
import { getUserById } from '../services/userService';
import Cookies from 'js-cookie';

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

function ShowDetails() {
  const { id } = useParams();
  const [show, setShow] = useState({});
  const [owner, setOwner] = useState({});
  const [currentUser, setCurrentUser] = useState({});
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({ name: '', description: '', category: '', image_url: null });
  const navigate = useNavigate();

  useEffect(() => {
    const fetchShow = async () => {
      try {
        const response = await getShowById(id);
        setShow(response);
        setFormData({ name: response.name, description: response.description, category: response.category });
        if (response.owner_id) {
          const ownerResponse = await getUserById(response.owner_id);
          setOwner(ownerResponse);
        }
        const currentUserID = Cookies.get('userToken');
        if (currentUserID) {
          const currentUserResponse = await getUserById(currentUserID);
          setCurrentUser(currentUserResponse);
        }
      } catch (error) {
        console.error(error);
      }
    };
    fetchShow();
  }, [id]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFileChange = (e) => {
    setFormData({ ...formData, image_url: e.target.files[0] });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      // console.log(formData, id)
      await updateShowById(id, formData);
      setShow(formData)
      setIsEditing(false);
    } catch (error) {
      console.error('Failed to update show', error);
    }
  };

  const handleDelete = async () => {
    try {
      await deleteShowById(id);
      navigate('/shows');
    } catch (error) {
      console.error('Failed to delete show', error);
    }
  };

  return (
    <div className="show-details-container">
      <Link to="/shows"><p className="back-link">Back</p></Link>
      <div className="show-details-card">
        {show.image_url && <img src={`http://localhost:8000/uploads/${show.image_url}`} alt={show.name} className="show-photo" />}
        <h1>{show.name}</h1>
        <p className="show-description">{show.description}</p>
        <p className="show-category">Category: {show.category}</p>
        {owner && (
          <div className="show-owner">
            <h2>Owner</h2>
            <p>{owner.username}</p>
            <p>{owner.email}</p>
          </div>
        )}
        {currentUser._id === show.owner_id && (
          <div className="show-actions">
            {isEditing ? (
              <form onSubmit={handleFormSubmit}>
                <label>Name:</label>
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                />
                <br />
                <label>Description:</label>
                <textarea
                  name="description"
                  value={formData.description}
                  onChange={handleInputChange}
                />
                <br />
                <label>Category:</label>
                <select name="category" value={formData.category} onChange={handleInputChange}>
                  <option value="">Select a category</option>
                  {categories.map(category => (
                    <option key={category} value={category}>{category}</option>
                  ))}
                </select>
                <br />
                <label>Photo:</label>
                <input
                  type="file"
                  name="image_url"
                  onChange={handleFileChange}
                />
                <br />
                <button type="submit" className="save-button">Save Changes</button>
                <button type="button" className="cancel-button" onClick={() => setIsEditing(false)}>Cancel</button>
              </form>
            ) : (
              <>
                <button className="edit-button" onClick={() => setIsEditing(true)}>Edit</button>
                <button className="delete-button" onClick={handleDelete}>Delete</button>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default ShowDetails;