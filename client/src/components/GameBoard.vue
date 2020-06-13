<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    {{items}}
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
      <button @click="getRandomTopic" class="rando-button" type="button">
        Get a Random Topic
      </button>
      <h2 v-if="userTopic">{{ userTopic }}</h2>
      <h2 v-else>
        <div>{{ RandomTopic }}</div>
      </h2>
    </div>

<div class="game-board">
    <div v-for="(item, index) in items" :key="index">
      <div class="grid-item">
        <input @keyup.enter="sendItems()" type="text" placeholder="Enter word" v-model="items[index]"/>
          {{items[index]}}
      </div>
    </div>
    <!-- make the conversation boxes for player 'challenges' -->
  </div>
  </div>
  <!-- </div> -->
</template>

<script>
import axios from "axios";
import io from 'socket.io-client';
var socket = io.connect('http://127.0.0.1:5000');

export default {
  name: "GameBoard",
  props: {
    title: String,
  },
  data() {
    return {
      isConnected: false,
      userTopic: "",
      RandomTopic: "",
      submittedItem: '',
      currentItem: '',
      items: ['','','','','','','','','','','','','','','','','','','','','','','','',''],
      submittedIndex: 0,
      playedWord: "",
      officialGameTopic: "",
      item1Word: "",
      item2Word: "",
    };
  },
  methods: {
    getRandomTopic() {
      axios
        .post("/gettopics", { RandomTopic: this.RandomTopic })
        .then((resp) => {
          let topicList = resp.data;
          let result = [];
          for (let i = 0; i < topicList.length; i++) {
            result.push(topicList[i]["topics"]);
          }
          let randTopicSelection = Math.floor(Math.random() * result.length);
          this.RandomTopic = result[randTopicSelection];
        })
        .catch((error) => console.log("error", error));
    },
    //adds the user-entered topic to the db
    addTopicToDB() {
      axios.post("/addtopic", { topic: this.userTopic });
      this.sendItems()
    },
    sendItems() {
      console.log('function called')
      socket.emit('item1', this.items);
    },
  },
  mounted() {
  socket.on('message', (message) => {
    this.items = message
    this.submittedItem = message
  })
  },
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
