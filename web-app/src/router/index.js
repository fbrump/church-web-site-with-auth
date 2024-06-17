import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import SmallGroupView from '../views//small-groups/SmallGroupsView.vue'
import SmallGroupDetailsView from '../views//small-groups/SmallGroupDetailsView.vue'
import LogInView from '@/views/auth/LogInView.vue'
// import { getToken } from '@/resources/auth'
import { useAuthStore } from '@/store/auth'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/small-groups',
      name: 'small-groups',
      component: SmallGroupView,
      meta: { requiresAuth: true },
    },
    {
      path: '/small-groups/:id',
      name: 'small-groups-details',
      component: SmallGroupDetailsView,
      props: true,
      meta: { requiresAuth: true },
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    }
  ]
})


router.beforeEach(async (to, from)=> {
  const authStore = useAuthStore();
	if (to.meta?.requiresAuth ) {
    // if (authStore.getCurrentToken === null){
    //   await getToken()
    //   .then((response) => {
    //     authStore.updateToken(response.data);
    //   })
    //   .catch((error) => console.error(error));
    // }
    
		if (!authStore.isAuthenticated) return '/login';
	}
  else{
    console.info("NOT requires AUTH")
  }
});

export default router
