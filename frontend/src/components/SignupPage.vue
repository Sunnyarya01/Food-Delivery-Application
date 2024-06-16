<template>
    <div>
      <h2>Sign Up</h2>
      <form @submit.prevent="signupUser">
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <input type="password" value="" placeholder="Confirm Password">
        <button type="submit">Sign Up</button>
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
      async signupUser() {
        const userData = {
          username: this.username,
          password: this.password,
        };
        try {
          const response = await this.$store.dispatch('signup', userData);
          console.log('Signed up:', response);
          // Optionally handle response and navigate
        } catch (error) {
          console.error('Sign up failed:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
    form {
      display: flex;
      flex-direction: column;
      align-items: center;
      border: 1px solid #ccc;
      width: 300px;
    }
  </style>
  