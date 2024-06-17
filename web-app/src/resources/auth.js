import axios from 'axios';


// const USERNAME = 'admin';
// const PASSWORD = 'Admin@1234'
const SCOPES = [
  'small-group:read',
  // 'address:read'
]

const getToken = async (username, password) => {
  return await axios
    .post('http://localhost:8000/api/v1/accounts/token', {
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