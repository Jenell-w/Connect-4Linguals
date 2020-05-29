<template>
  <div id="app">
    <GameBoard title="Ready to Play Connect 4 Linguals?" />
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
