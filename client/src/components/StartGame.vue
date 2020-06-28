<template>
  <div>
    <div id="directions" class="modal" ref="modal">
      <!-- Modal content -->
      <div class="modal-content" ref="modalContent">
        <div class="modal-body">
          <span @click="$refs.modal.style.display='none'" class="close">&times;</span>
          <button class="directions-button" @click="getDirections">How Do I Play?{{this.modalText}}</button>
        </div>
      </div>
    </div>
    <div v-if="showStartGameInfo" class="Startgame">
      <div class="dropdown">
        <p>Pick a Player to play against!</p>
        <select id="player-list" @change="getPlayer2()" v-model="player" name="Select an opponent">
          <option v-for="player in playerList" :key="player" :value="player">{{ player }}</option>
        </select>
      </div>

      <div class="enter-topics-container">
        <h3>Enter a topic and press enter!</h3>
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
        <button class="playnow" @click="playNow" type="button">Play Now!</button>
      </div>
    </div>
    <GameBoard 
      v-if="showBoard" 
      :gameData="gameData"
      :room="room"
      :userSessionID='userSessionID'
    />
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
    title1: String,
    userSessionID: String,
  },
  components: {
    GameBoard
  },
  data() {
    return {
      userTopic: "",
      RandomTopic: "",
      playerList: [],
      player: "",
      player2: "",
      officialGameTopic: "",
      showBoard: false,
      showStartGameInfo: true,
      modalText: "",
      Directions: "Directions for Game Play",
      gameData: null,
      room: null,
    };
  },
  methods: {
    getDirections() {
      this.modalText =
        "Select an available opponent to play against and a game topic.  Then, each player will enter a word relating to the topic in a box so as to get 4 in a row in any direction. Players have the option to 'challenge' the item written.";
      this.openModal();
    },
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
    },
    //the current user in session is coming up in this list
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
          let avail_players = all_users.filter(
            item => !active_players.includes(item)
          );
          this.playerList = avail_players;
        });
    },
    getPlayer2() {
      return this.player;
    },
    playNow() {
      this.officialGameTopic = this.userTopic + this.RandomTopic;
      console.log("playnow official game topic,", this.officialGameTopic);
      axios.post("/startgame", {
        player: this.player,
        officialGameTopic: this.officialGameTopic
      }).then(() => {
        this.checkIfGame()
      })
    },
    openModal() {
      let modal = this.$refs.modal;
      let modalContent = this.$refs.modalContent;
      modal.style.display = "block";
      setTimeout(function() {
        modalContent.classList.add("animate-down");
        modal.classList.add("fade-out");
      }, 20000);
      setTimeout(function() {
        modal.style.display = "none";
      }, 20000);
      modal.classList.remove("animate-down");
      modal.classList.remove("fade-out");
    },

    checkIfGame() {
      axios.get("/checkifingame")
      .then(resp => {
        if (resp.data.success.game === "nogame") {
          this.showBoard = false;
          this.showStartGameInfo = true;
        } else {
          this.showBoard = true;
          this.showStartGameInfo = false;
          this.gameData = resp.data.success
          socket.emit('join', this.userSessionID);
        }
      });
    }
  },
  mounted() {
    this.getPlayerList();
    this.checkIfGame();
  }
};
</script>

<style>
#directions {
  text-align: center;
  justify-content: center;
}
</style>
