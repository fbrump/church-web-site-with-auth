import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import SmallGroupView from '../views//small-groups/SmallGroupsView.vue'
import SmallGroupDetailsView from '../views//small-groups/SmallGroupDetailsView.vue'
import LogInView from '@/views/auth/LogInView.vue'

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
      component: SmallGroupView
    },
    {
      path: '/small-groups/:id',
      name: 'small-groups-details',
      component: SmallGroupDetailsView,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    }
  ]
})

export default router
