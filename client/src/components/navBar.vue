<template>
  <div class="routers">
    <nav id="home-login-register-logout">
      <router-link tag="button" class="button" v-if="this.checksession = false" to="/">Home</router-link>
      <br />
      <br />
      <router-link tag="button" class="button" v-if="!checksession" to="/login">Login</router-link>
      <br />
      <br />
      <router-link tag="button" class="button" v-if="!checksession" to="/register">Register</router-link>
      <br />
      <br />
      <button class="button" v-if="checksession">
        <a @click="logOut">
          <span>Logout</span>
        </a>
      </button>
    </nav>
  </div>
</template>

<script>
import { isAuthenticated } from "../views/helpers";
import axios from "axios";
import { globalSessionVar } from "../main";

export default {
  name: "App",
  data() {
    return {
      checksession: false
    };
  },
  methods: {
    logOut() {
      axios.get("logout").then(() => {
        this.$router.push("/login");
        this.checksession = false;
      });
    }
  },
  created() {
    globalSessionVar.$on("login", () => {
      this.checksession = true;
    });
  },
  mounted() {
    isAuthenticated().then(data => {
      if (data["session"] === true) {
        this.checksession = true;
      }
    });
  }
};
</script>

<style>
#home-login-register-logout {
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  flex-direction: row;
  -webkit-box-align: start;
  align-items: flex-start;
}
</style>