import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/components/LandingPage.vue';
import LoginPage from '@/components/LoginPage.vue';
import SignupPage from '@/components/SignupPage.vue';

const routes = [
  { path: '/', component: LandingPage },
  { path: '/login', component: LoginPage },
  { path: '/signup', component: SignupPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
