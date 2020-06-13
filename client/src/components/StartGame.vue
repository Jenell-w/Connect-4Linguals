<template>
  <div>
    <div class="dropdown">
      <p>Pick a Player to play against!</p>
      <form>
        <select name="dropdown">
          <option value="Players" selected>Player List</option>
        </select>
      </form>
      <button @click="getPlayerList">get list</button>
      {{ playerList }}
    </div>
    <div class="enter-topics-container">
      <h3>Enter a topic</h3>
      <input
        v-model="userTopic"
        @keyup.enter="addTopicToDB"
        type="text"
        name="user-topic"
        id="user-topic"
      />
      <br />
      <br />
      <h3>OR</h3>
      <button @click="getRandomTopic" class="rando-button" type="button">Get a Random Topic</button>
      <h2 v-if="userTopic">{{ userTopic }}</h2>
      <h2 v-else>
        <div>{{ RandomTopic }}</div>
      </h2>
    </div>
    <GameBoard />
  </div>
</template>

<script>
import axios from "axios";
import GameBoard from "../components/GameBoard";
import io from "socket.io-client";
var socket = io.connect("http://127.0.0.1:5000");

export default {
  name: "StartGame",
  props: {
    title1: String
  },
  components: {
    GameBoard
  },
  data() {
    return {
      userTopic: "",
      RandomTopic: "",
      playerList: ""
    };
  },
  methods: {
    getRandomTopic() {
      axios
        .post("/gettopics", { RandomTopic: this.RandomTopic })
        .then(resp => {
          let topicList = resp.data;
          let result = [];
          for (let i = 0; i < topicList.length; i++) {
            result.push(topicList[i]["topics"]);
          }
          let randTopicSelection = Math.floor(Math.random() * result.length);
          this.RandomTopic = result[randTopicSelection];
        })
        .catch(error => console.log("error", error));
    },
    //adds the user-entered topic to the db
    addTopicToDB() {
      axios.post("/addtopic", { topic: this.userTopic });
      //this.sendItems();
    },
    getPlayerList() {
      axios
        .post("/playerlist", { playerList: this.playerList })
        .then(resp => {
          let playerList = resp.data;
          this.playerList = resp.data;
          let result = [];
          for (let i = 0; i < playerList.length; i++) {
            result.push(playerList[i].Player1_username);
          }
          console.log(result);
          result = getPlayerList.json;
          console.log(getPlayerList);
        })

        .catch(error => console.log("error", error));
    },
    sendItems() {
      socket.emit("item1", this.items);
    }
  }
};
</script>

<style></style>
