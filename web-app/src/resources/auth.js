import axios from 'axios';
import getHeaders from '.';

const SCOPES = [
  'small-group:read'
]

const getToken = async (username, password) => {
  return await axios
    .post('/api-auth/accounts/token', {
      username: username,
      password: password,
      scope: SCOPES.join(' ')
    }, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
};

const getUser = async () => {
  return await axios
    .get('/api-auth/accounts/users/me/', {
      headers: getHeaders()
    });
};

export { getToken, getUser };