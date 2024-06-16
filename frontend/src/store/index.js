import { createStore } from 'vuex';
import axios from 'axios';

const apiUrl = 'http://localhost:8000/api';

const store = createStore({
  state: {
    token: null,
    user: null,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    setUser(state, user) {
      state.user = user;
      localStorage.setItem('user', JSON.stringify(user));
    },
    logout(state) {
      state.token = null;
      state.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post(`${apiUrl}/token`, credentials);
        const { token } = response.data;
        commit('setToken', token);
        return token;
      } catch (error) {
        console.error('Error logging in:', error);
        throw error;
      }
    },
    async signup(_, userData) {
      try {
        const response = await axios.post(`${apiUrl}/create`, userData);
        return response.data;
      } catch (error) {
        console.error('Error signing up:', error);
        throw error;
      }
    },
    logout({ commit }) {
      commit('logout');
    },
  },
  modules: {},
});

const token = localStorage.getItem('token');
if (token) {
  store.commit('setToken', token);
}

export default store;
