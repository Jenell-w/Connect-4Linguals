<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <div class="enter-topics-container">
      <h3>Enter a topic</h3>
      <input v-model="userTopic" type="text" name="user-topic" id="user-topic" />
      <br />
      <br />
      <input type="submit" value="Play Game!" />
      <h3>OR</h3>
      <button v-on:click="getRandomTopic" class="rando-button" type="button">Get a Random Topic</button>
      <h2 v-if="userTopic">{{ userTopic }}</h2>
      <div v-else>{{ RandomTopic }}</div>
    </div>
    <div class="game-board">
      <div class="grid-item">
        <!-- create "@keyupenter"- word is submitted -->
        <input id="item-1" type="text" placeholder="Enter word" />
        <br />
        <input type="submit" value="Play Word" />
      </div>
      <div class="grid-item">
        <input id="item-2" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-3" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-4" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-5" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-6" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-7" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-8" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-9" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-10" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-11" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-12" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-13" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-14" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-15" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-16" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-17" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-18" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-19" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-20" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-21" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-22" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-23" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-24" type="text" placeholder="Enter word" />
      </div>
      <div class="grid-item">
        <input id="item-25" type="text" placeholder="Enter word" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GameBoard",
  props: {
    title: String
  },
  data() {
    return {
      userTopic: "",
      RandomTopic: ""
    };
  },
  methods: {
    getRandomTopic() {
      axios
        .post("https://conn-linguals-ConnectLinguals.harperdbcloud.com")
        .then(response => (this.RandomTopic = response));
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  text-align: center;
}
.game-board {
  display: grid;
  grid-gap: 2rem;
  background-color: #2196f3;
  margin: 10px;
  border: solid 2px darkgrey;
  justify-content: center;
  grid-template-columns: repeat(5, 10vw);
  grid-template-rows: repeat(5, 10vw);
}
.grid-item:nth-child(1) {
  grid-row: 1;
  grid-column: 1;
}
.grid-item:nth-child(2) {
  grid-row: 1;
  grid-column: 2;
}
.grid-item:nth-child(3) {
  grid-row: 1;
  grid-column: 3;
}
.grid-item:nth-child(4) {
  grid-row: 1;
  grid-column: 4;
}
.grid-item:nth-child(5) {
  grid-row: 1;
  grid-column: 5;
}
.grid.item {
  display: flex;
  align-items: center;
  justify-content: center;
  border: darkgrey;
}
</style>
