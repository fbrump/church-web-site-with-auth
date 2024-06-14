import axios from 'axios';


const getAll = async () => {
  return axios
    .get('/api/small-groups/small-groups/?skip=0&limit=100', {
      headers: {
        'Content-Type': 'application/json'
      }
    });
};

export { getAll };