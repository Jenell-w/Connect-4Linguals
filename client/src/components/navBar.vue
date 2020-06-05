<template>
  <div>
    <router-link to="/">Home</router-link><br>
    <router-link  to="/login">Login</router-link><br>
    <router-link  to="/register">Register</router-link><br><br>
    <button v-if='checksession' ><a @click='logOut'><span>Logout</span></a></button>
  </div>
</template>

<script>
import { isAuthenticated } from '../views/helpers';
import axios from 'axios'

export default {
  name: "App",
  data() {
    return {
      checksession: false,
    }
  },
  methods: {
    logOut() {
      axios.get('logout')
      .then(() => {
        this.$router.push('/login')
        this.checksession = false
        })
    }
  },
  mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === true) {
        this.checksession = true
      }
    })
  }
};
</script>

<style>
</style>