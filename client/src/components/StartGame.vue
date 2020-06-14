<template>
  <div>
    <div class="dropdown">
      <p>Pick a Player to play against!</p>
      <select id="player-list" v-model="playerList" name="Select an opponent">
        <option v-for="player in playerList" :value="player" :key="player">{{ player }}</option>
      </select>
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
      playerList: [],
      player: ""
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
        .all([axios.post("/currentplayerlist"), axios.post("/userlist")])
        .then(respArr => {
          let currentPlayerList = respArr[0].data;
          let allUserList = respArr[1].data;
          let active_players = [];
          let all_users = [];
          for (let i = 0; i < currentPlayerList.length; i++) {
            active_players.push(currentPlayerList[i].Player1_username);
            active_players.push(currentPlayerList[i].Player2_username);
          }
          //active_players is list of current players
          //all_users is a list of all users
          for (let i = 0; i < allUserList.length; i++) {
            all_users.push(allUserList[i].username);
          }
          //this shoudl take out those in active_players but it is not working
          let avail_players = all_users.filter(
            item => !active_players.includes(item.username)
          );
          console.log(avail_players);
          this.playerList = avail_players;
          this.player = this.playerList[0].username;
        });
    },
    sendItems() {
      socket.emit("item1", this.items);
    }
  },
  mounted() {
    this.getPlayerList();
  }
};
</script>

<style></style>
