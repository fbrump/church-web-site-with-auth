import axios from 'axios';


const getAll = async () => {
  axios
    .get('/api/small-groups/small-groups/?skip=0&limit=100', {
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