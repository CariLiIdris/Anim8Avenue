import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getShowById } from '../services/showService';

function ShowDetails() {
  const { id } = useParams();
  const [show, setShow] = useState({});

  useEffect(() => {
    const fetchShow = async () => {
      try {
        const response = await getShowById(id);
        setShow(response);
      } catch (error) {
        console.error(error);
      }
    };
    fetchShow();
  }, [id]);

  return (
    <div>
      <h1>{show.name}</h1>
      <p>{show.description}</p>
    </div>
  );
}

export default ShowDetails