import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { getToken } from '@/resources/auth';
import router from '@/router';


export const useAuthStore = defineStore('auth', () => {
  // state
  const authenticated = ref(false); 
  const user = ref(null);
  const token = ref(null);

  // getters
  const isAuthenticated = computed(() => authenticated.value);
  const getLogedUser = computed(() => user.value);
  const getCurrentToken = computed(() => token.value);

  // actions
  const updateToken = (data_token) => {
    token.value = data_token;
    authenticated.value = true;
  }

  const login = async (username, password) => {
    await getToken(username, password)
    .then((response) => {
      updateToken(response.data);
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

    router.push('/login');
  }

  return { 
    authenticated, user, token, 
    getCurrentToken,
    getLogedUser, 
    isAuthenticated,
    updateToken,
    login,
    logout,
  }
});