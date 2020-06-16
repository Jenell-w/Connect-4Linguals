<template>
  <div class="hello">
    <h1>Topic: {{gameData.official_game_topic}}</h1>
    <br />
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
          {{ gameboardData[index]}}
        </div>
      </div>
    </div>
    <div class="challenge-word">
      <label for="challenge-other-players-word">Challenge Your Opponent's Latest Entry:</label>
      <br />
      <select
        class="challenge"
        @change="submitChallengeReasons()"
        name="challenge-other-players-word"
        v-model="reason"
      >
        <option v-for="reason in challengeReasons" :key="reason" :value="reason">{{ reason }}</option>
      </select>
      <br />
      <span class="reason">{{ gameData.challenge_reason }}</span>
      <br />
      <div v-if="reason === 'Other'" class="challenge-comment-box">
        <label for="challenge-comment">Comment/Other Reason for Challenge:</label>
        <br />
        <span class="challenge-comment">{{ gameData.challenge_comments }}</span>
        <br />
        <textarea
          @keyup.enter="submitChallengeReasons"
          v-model="challengeComment"
          name="other-challenge"
          rows="4"
          cols="50"
        ></textarea>
        <br />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import io from "socket.io-client";
var socket = io.connect("http://127.0.0.1:5000");

export default {
  name: "GameBoard",
  props: {
    title: String,
    gameData: Object
  },
  data() {
    return {
      isConnected: false,
      challengeReasons: [
        "Spelling error",
        "Off-topic",
        "Invalid entry",
        "Other"
      ],
      reason: "",
      challengeComment: "",
      submittedItem: "",
      currentItem: "",
      gameboardData: [],
      submittedIndex: 0,
      officialGameTopic: ""
    };
  },
  methods: {
    submitChallengeReasons() {
      axios.post("/userchallenge", {
        reason: this.reason,
        challengeComment: this.challengeComment
      });
    },
    sendItems() {
      socket.emit("gameboard", this.gameboardData);
    },
    changeGameboardToArray() {
      this.gameboardData = this.gameData.board
        .replace("[", "")
        .replace("]", "")
        .split(",");
    }
  },
  mounted() {
    socket.on("gameboard", message => {
      this.gameboardData = message;
    });
    this.changeGameboardToArray();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
.reason,
.challenge-comment {
  text-align: center;
  margin: 20px;
  justify-content: center;
  font-style: italic;
  font-weight: bold;
}
.challenge-word {
  text-align: center;
  margin: 20px;
  justify-content: center;
}
.grid-item {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}
</style>
