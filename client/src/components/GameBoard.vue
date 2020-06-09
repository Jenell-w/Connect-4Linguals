<template>
  <div class="hello">
    <h1>{{ title }}</h1>
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
      <button class="play-now-topic" @click="playNow">Play Now!</button>
    </div>
    <div class="game-board">
      <div class="grid-item">
        <input
          @keyup.enter="gameplayEntry()"
          v-model="item1Word"
          id="item-1"
          type="text"
          placeholder="Enter word"
        />
        <p>{{ item1Word }}</p>
        <br />
      </div>
      <div class="grid-item">
        <input
          @keyup.enter="gameplayEntry()"
          v-model="item2Word"
          id="item-2"
          type="text"
          placeholder="Enter word"
        />

        <p>{{ item2Word }}</p>
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
    <!-- make the conversation boxes for player 'challenges' -->
  </div>
</template>

<script>
import axios from "axios";

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
      playedWord: "",
      officialGameTopic: "",
      item1Word: "",
      item2Word: "",
      item3: "",
      item4: "",
      item5: "",
      item6: "",
      item7: "",
      item8: "",
      item9: "",
      item10: "",
      item11: "",
      item12: "",
      item13: "",
      item14: "",
      item15: "",
      item16: "",
      item17: "",
      item18: "",
      item19: "",
      item20: "",
      item21: "",
      item22: "",
      item23: "",
      item24: "",
      item25: "",
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
    },

    gameplayEntry() {
      axios.post("/enterword", { item1WordEntered: this.item1Word });
    },
    playNow() {
      if (this.RandomTopic != "") {
        this.officialGameTopic = this.userTopic;
      } else {
        this.officialGameTopic = this.RandomTopic;
      }
      console.log(this.officialGameTopic);
      axios.post("/playnow", {
        officialGameTopicEntry: this.officialGameTopic,
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  text-align: center;
}
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
