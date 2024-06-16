<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async loginUser() {
        const credentials = {
          username: this.username,
          password: this.password,
        };
        try {
          const token = await this.$store.dispatch('login', credentials);
          console.log('Logged in. Token:', token);
          this.$router.push('/');
        } catch (error) {
          console.error('Login failed:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add scoped styles */
  </style>
  