import axios from 'axios';


const getAll = async () => {
  axios
    .get('http://localhost:8000/api/v1/small-groups/small-groups/?skip=0&limit=100', {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then((response) => {
      console.log(response.data)
    })
    .catch((error) => console.error(error));
};

export { getAll };