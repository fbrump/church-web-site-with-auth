import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { getToken, getUser } from '@/resources/auth';
import router from '@/router';


const USER_TOKEN_KEY = 'user-token';

export const useAuthStore = defineStore('auth', () => {
  // state
  const authenticated = ref(false); 
  const user = ref(null);
  const token = ref(JSON.parse(localStorage.getItem(USER_TOKEN_KEY)));

  // getters
  const isAuthenticated = computed(() => authenticated.value);
  const getLogedUser = computed(() => user.value);
  const getCurrentToken = computed(() => token.value);

  // actions
  const updateToken = (data_token) => {
    token.value = data_token;
    authenticated.value = true;
    localStorage.setItem(USER_TOKEN_KEY, JSON.stringify(token.value));
  }

  const updateUser = async () => {
    await getUser()
    .then((response) => {
      user.value = response.data;
      authenticated.value = true;
    })
    .catch((error) => {
      console.error(error);
    });
  }

  const login = async (username, password) => {
    await getToken(username, password)
    .then((response) => {
      updateToken(response.data);
      updateUser();
      router.push('/');
    })
    .catch((error) => {
      console.error(error);
      router.push('/login');
    });
  }

  const logout = () => {
    console.log('logout')
    authenticated.value = false;
    user.value = null;
    token.value = null;
    localStorage.removeItem(USER_TOKEN_KEY);
    router.push('/login');
  }

  return { 
    authenticated, user, token, 
    getCurrentToken,
    getLogedUser, 
    isAuthenticated,
    updateToken,
    updateUser,
    login,
    logout,
  }
});