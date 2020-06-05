<template>
<div class=register-box>
  <div class="register-form">
    <p class='error' v-if='error'>{{error}}</p>
    <input @keyup.enter.exact='addUser' type="text" v-model="username" placeholder="Username"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="password" placeholder="Password"/>
    <input @keyup.enter.exact='addUser' type="password" v-model="retypePassword" placeholder="Retype Password"/>
    <button @click="addUser">Register</button>
    <div class='sign-up-btn'>Already have an account?<a href="/login"> Login</a></div>
  </div>
</div>
</template>

<script>
import axios from "axios";
export default {
    name: "register",
    data() {
    return {
      username: '',
      password: '',
      retypePassword:'',
      error: '',
      code: '',
    }
  },
  methods: {
    /* add a new user, note there is no 
    client side validation in place yet...*/ 
    addUser() {
      if (this.password == this.retypePassword) {
        axios.post('userregister', {
        username: this.username, 
        password: this.password,
        })
        .then(response => {
            if (response.data.success == false) {
                this.$router.push({ path: '/register'})
                this.error = 'Username already exists'
            } else {
                this.username = '';
                this.password = '';
                /* this setTimeout() allows for the session to be set and then will redirect*/
                setTimeout(() => this.$router.push({ path: '/'}), 500);
            }
        console.log(response);
        })
        .catch(error => {
        console.log(error);
      });
      } else {
        this.error = 'Passwords do not match'
      }
    }
  },
}
</script>


<style></style>