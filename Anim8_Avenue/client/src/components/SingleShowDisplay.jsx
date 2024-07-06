import React from 'react';

const SingleShowDisplay = ({ setTitle }) => {
  // assumes you have a way to get the show ID from the URL
  const showId = useParams()._id;
  const [show, setShow] = useState({});

  useEffect(() => {
    axios.get(`/api/shows/${showId}`)
      .then(response => {
        setShow(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, [showId]);

  return (
    <div>
      <h2>{show.name}</h2>
      <p>{show.description}</p>
    </div>
  );
};

export default SingleShowDisplay