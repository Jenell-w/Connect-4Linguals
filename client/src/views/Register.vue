<template>
  <div class="register-box">
    <div class="register-form">
      <p class="error" v-if="error">{{error}}</p>
      <input @keyup.enter.exact="addUser" type="text" v-model="username" placeholder="Username" />
      <input @keyup.enter.exact="addUser" type="password" v-model="password" placeholder="Password" />
      <input
        @keyup.enter.exact="addUser"
        type="password"
        v-model="retypePassword"
        placeholder="Retype Password"
      />
      <button id="button" @click="addUser">Register</button>
      <div class="sign-up-btn">
        Already have an account?
        <a href="/login">Login</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { globalSessionVar } from "../main";

export default {
  name: "register",
  data() {
    return {
      username: "",
      password: "",
      retypePassword: "",
      error: "",
      code: ""
    };
  },
  methods: {
    /* add a new user, note there is no 
    client side validation in place yet...*/

    addUser() {
      if (this.password == this.retypePassword) {
        axios
          .post("userregister", {
            username: this.username,
            password: this.password
          })
          .then(response => {
            if (response.data.success == false) {
              this.$router.push({ path: "/register" });
              this.error = "Username already exists";
            } else {
              this.username = "";
              this.password = "";
              globalSessionVar.$emit("login");
              /* this setTimeout() allows for the session to be set and then will redirect*/
              setTimeout(() => this.$router.push({ path: "/" }), 1000);
            }
            console.log(response);
          })
          .catch(error => {
            console.log(error);
          });
      } else {
        this.error = "Passwords do not match";
      }
    }
  }
};
</script>


<style>
button,
#button {
  box-shadow: 3px 4px 0px 0px #899599;
  background: linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);
  background-color: #ededed;
  border-radius: 15px;
  border: 1px solid #d6bcd6;
  display: inline-block;
  cursor: pointer;
  color: #3a8a9e;
  font-family: Arial;
  font-size: 17px;
  padding: 7px 25px;
  text-decoration: none;
  text-shadow: 0px 1px 0px #e1e2ed;
}
</style>