import { useAuthStore } from "@/store/auth"; 

const getHeaders = () =>  {
  const authStore = useAuthStore();

  const headers = {
    'Content-Type': 'application/json'
  };

  if (authStore.isAuthenticated)
  {
    headers['Authorization'] = 'Bearer ' + authStore.token; 
  }
  
  return headers;
};

export default getHeaders;