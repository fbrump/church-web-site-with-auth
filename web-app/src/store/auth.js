import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { getToken } from '@/resources/auth';


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
    })
    .catch((error) => console.error(error));
  }

  const logout = () => {
    isAuthenticated.value = false;
    user = null;
    token = null;
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