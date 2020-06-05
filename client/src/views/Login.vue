<template>
    <div class='login-box'>
        <div class="login-form">
            <input @keyup.enter.exact='checkUser' type="text" v-model="username" placeholder="Username"/>
            <input @keyup.enter.exact='checkUser' type="password" v-model="password" placeholder="Password"/>
            <button @click="checkUser" >Login</button>
            <div class ='sign-up-btn'>Don't have an account?<a href="/register"> Sign Up</a></div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "login",
    data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    /* authenticates the user in the db */
    checkUser() {
      axios.post('userlogin', {
        username: this.username, 
        password: this.password
        })
        .then(function (response) {
        console.log(response);
        })
        .catch(function (error) {
        console.log(error);
      });
      this.username = '';
      this.password = '';
      /* this setTimeout() allows for the session to be set and then will redirect*/
      setTimeout(() => this.$router.push({ path: '/'}), 1000);
    }
  }
}
</script>