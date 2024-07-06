import React from 'react';
import axios from 'axios';

function ShowDetails(props) {
  const [show, setShow] = useState({});

  useEffect(() => {
    axios.get(`/api/shows/${props.match.params.id}`)
      .then(response => {
        setShow(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, [props.match.params.id]);

  return (
    <div>
      <h1>{show.name}</h1>
      <p>{show.description}</p>
    </div>
  );
}

export default ShowDetails;