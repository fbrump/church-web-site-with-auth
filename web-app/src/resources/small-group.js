import axios from 'axios';
import getHeaders from '.';


const getAll = async () => {
  return axios
    .get('/api/small-groups/small-groups/?skip=0&limit=100', {
      headers: getHeaders()
    });
};

const getById = async (id) => {
  return axios
    .get('/api/small-groups/small-groups/' + id, {
      headers: getHeaders()
    });
};

export { getAll, getById };