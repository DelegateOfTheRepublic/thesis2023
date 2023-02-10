import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';
const API_AUTH_URL = 'http://localhost:8000/api/auth/token/'

class AuthService {
  async login(user) {
    const response = await axios
          .post(API_AUTH_URL + 'login', {
              username: user.username,
              password: user.password
          });
      if (response.data.token) {
          localStorage.setItem('user', JSON.stringify(response.data));
      }
      return response.data;
  }

  logout() {
    localStorage.removeItem('user');
  }
}

export default new AuthService();