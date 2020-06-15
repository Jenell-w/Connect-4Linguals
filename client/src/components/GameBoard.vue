<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    {{items}}
    <div class="game-board">
      <div v-for="(item, index) in items" :key="index">
        <div class="grid-item">
          <input
            @keyup.enter="sendItems()"
            type="text"
            placeholder="Enter word"
            v-model="items[index]"
          />
          {{items[index]}}
        </div>
      </div>
    </div>
    <!-- challenge boxes for players to contest a word -->
    <div id="challenge-word">
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
      <span class="reason">{{ reason }}</span>
      <br />
      <div v-if="reason === 'Other'" class="challenge-comment-box">
        <label for="challenge-comment">Comment/Other Reason for Challenge:</label>
        <br />
        <textarea v-model="challengeComment" name="other-challenge" rows="4" cols="50"></textarea>
        <br />
        <span class="challenge-comment">{{ challengeComment }}</span>
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
    title: String
  },
  data() {
    return {
      isConnected: false,
      reason: "",
      challengeReasons: [
        "Spelling error",
        "Off-topic",
        "Invalid entry",
        "Other"
      ],
      challengeComment: "",
      submittedItem: "",
      currentItem: "",
      items: [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
      ],
      submittedIndex: 0,
      officialGameTopic: ""
    };
  },
  //retrieve officialgame topic to post at top of board
  methods: {
    submitChallengeReasons() {
      axios.post("/userchallenge", {
        challengeReason: this.reason,
        challengeComment: this.challengeComment
      });
    },

    //need to make chat button
    //need to get current game baord to retrieve for prior users
    getCurrentGameBoard() {
      axios.post();
    },
    sendItems() {
      socket.emit("gameboard", this.items);
    }
  },
  mounted() {
    socket.on("message", message => {
      this.items = message;
      this.submittedItem = message;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
  margin: 10px;
  justify-content: center;
  font-style: italic;
}
</style>
