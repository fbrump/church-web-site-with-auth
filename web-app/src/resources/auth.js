import axios from 'axios';

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

export { getToken };