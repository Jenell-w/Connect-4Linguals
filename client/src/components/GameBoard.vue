<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <div class="game-board">
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="box"></div>
      <div class="wall"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="box"></div>
      <div class="wall"></div>
      <div class="box"></div>
      <div class="box"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
      <div class="wall"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameBoard",
  props: {
    title: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.game-board {
  display: grid;
  grid-template-columns: 20px 120px 120px 120px 120px 20px;
  grid-template-rows: 20px 120px 120px 120px 120px 20px;
  justify-content: center;
}
.wall {
  background-color: black;
}
.box {
  background-color: #d9d9d9;
  border: 2px solid black;
}
</style>
