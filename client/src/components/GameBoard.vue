<template>
  <div class="hello">
    <h1>Topic: {{gameData.official_game_topic}}</h1><br>
    <h3>Player1: {{gameData.Player1_username}}</h3>
    <h3>Player2: {{gameData.Player2_username}}</h3>
    <div class="game-board">
      <div v-for="(item, index) in gameboardData" :key="index">
        <div class="grid-item">
          <input
            @keyup.enter="sendItems()"
            type="text"
            placeholder="Enter word"
            v-model="gameboardData[index]"
          />
        </div>
      </div>
      <!-- make the conversation boxes for player 'challenges' -->
    </div>
  </div>
  <!-- </div> -->
</template>

<script>
import axios from "axios";
import io from "socket.io-client";
var socket = io.connect("http://127.0.0.1:5000");

export default {
  name: "GameBoard",
  props: {
    title: String,
    gameData: Object,
  },
  data() {
    return {
      isConnected: false,
      submittedItem: "",
      currentItem: "",
      gameboardData: [],
      submittedIndex: 0,
      officialGameTopic: ""
    };
  },
  //retrieve officialgame topic to post at top of board
  methods: {
    //need to make chat button
    //need to get current game baord to retrieve for prior users
    getCurrentGameBoard() {
      axios.post();
    },
    sendItems() {
      socket.emit("gameboard", this.gameboardData);
    },
    changeGameboardToArray() {
      this.gameboardData = this.gameData.board.replace('[', '').replace(']', '').split(',')
    }
  },
  mounted() {
    socket.on("gameboard", message => {
      this.gameboardData = message;
    });
    this.changeGameboardToArray()
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* h1,
h2 {
  text-align: center;
} */
.play-now-topic {
  display: flex;
  justify-content: center;
  align-items: center;
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
</style>
