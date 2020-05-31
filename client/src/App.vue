<template>
  <div id="app">
    <h1>Login</h1>
    <!-- Pete, work your magic! Can you make login boxes disappear after user is logged in? -->
    <form>
      <label for="username">Enter your username:</label>
      <input type="user" id="user" />
      <br />
      <br />
      <label for="pswd">Enter your password:</label>
      <input type="password" id="pswd" />
      <br />
      <br />
      <input type="button" value="Submit" />
    </form>
    <GameBoard title="Ready to Play Connect 4 Linguals???" />
  </div>
</template>

<script>
import GameBoard from "./components/GameBoard.vue";

export default {
  name: "App",
  components: {
    GameBoard
  }
};
</script>

<style></style>
