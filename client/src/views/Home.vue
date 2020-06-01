<template>
  <div id="app">
    <navBar/>
    <GameBoard title="Ready to Play Connect 4 Linguals???" />
  </div>
</template>

<script>
import GameBoard from "../components/GameBoard";
import navBar from "../components/navBar"

export default {
  name: "App",
  components: {
    GameBoard, navBar
  }
};
</script>

<style></style>
