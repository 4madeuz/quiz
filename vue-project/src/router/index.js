import { createRouter, createWebHistory } from 'vue-router'
import Surveys from '../views/Surveys.vue'
import SurveyView from '../views/SurveyView.vue'
import AppLayout from '@/layout/AppLayout.vue';
import SurveyViewTest from '../views/SurveyViewTest.vue'
import store from '@/store'; // NEW

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
    path: '/',
            component: AppLayout,
            children: [
              {
                path: '/surveys',
                name: 'Surveys',
                component: Surveys,
                meta: { requiresAuth: true },
              },
              {
                path: '/surveys/:id',
                name: 'Survey',
                component: SurveyView,
                meta: { requiresAuth: true },
              },
              {
                path: '/auth/login',
                name: 'login',
                component: () => import('@/views/auth/Login.vue')
            },
            {
              path: '/results/:id',
              name: 'Result',
              props: true,
              component: () => import('@/views/ResultView.vue'),
              meta: { requiresAuth: true },
          },
          {
            path: '/results',
            name: 'Results',
            component: () => import('@/views/Results.vue'),
            meta: { requiresAuth: true },
          },
          {
            path: '/user/self/results',
            name: 'UserResults',
            component: () => import('@/views/UserResultsView.vue'),
            meta: { requiresAuth: true },
          },
          ]
    }
  ]
})


router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/auth/login');
  } else {
    next();
  }
});


export default router
