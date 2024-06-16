import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the router configuration
import store from './store'; // Import the Vuex store
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

createApp(App)
  .use(router) // Use the router
  .use(store) // Use the Vuex store
  .mount('#app');
