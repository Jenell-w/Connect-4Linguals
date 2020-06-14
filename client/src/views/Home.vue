<template>
  <div id="app">
    <StartGame title1="Let's Start a Game" />
  </div>
</template>

<script>
import StartGame from "../components/StartGame";
import { isAuthenticated } from "./helpers";

export default {
  name: "App",
  components: {
    StartGame
  },
  data() {
    return {
      message: "",
      messageList: []
    };
  },
  mounted() {
    isAuthenticated().then(data => {
      if (data["session"] === false) {
        this.$router.push("/login");
      } else {
        this.userSessionID = data["user"];
      }
    });
  }
};
</script>

<style></style>
