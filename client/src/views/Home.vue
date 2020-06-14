<template>
  <div id="app">
    <StartGame title1="Let's Start a Game" />
    <!-- <GameBoard title="Play Connect 4 Linguals" /> -->
    <!-- <div>
      <input type="text" v-model="message"/>
      <button @click='sendMessage'>Submit</button>
      <br>
      {{messageList}}
    </div>-->
  </div>
</template>

<script>
import GameBoard from "../components/GameBoard";
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
    })
  }
};
</script>

<style></style>
