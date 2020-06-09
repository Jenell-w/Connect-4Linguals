<template>
  <div id="app">
    <GameBoard title="Play Connect 4 Linguals" />
    <!-- <div> -->
      <!-- <input type="text" v-model="message"/>
      <button @click='sendMessage'>Submit</button>
      <br>
      {{messageList}}
    </div> -->
  </div>
</template>

<script>
import GameBoard from "../components/GameBoard";
import { isAuthenticated } from './helpers';
import io from 'socket.io-client';
var socket = io.connect('http://127.0.0.1:5000');

export default {
  name: "App",
    components: {
    GameBoard
  },
  data() {
    return {
      message: '',
      messageList: [],
    }
  },
  methods: {
      sendMessage() {
          socket.emit('message', this.message);
          this.message = '';
      },
  },
  created(){
    
  },
  mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      } else {
        this.userSessionID = data['user']
      }
    })
    socket.on('message', (message) => {
        this.messageList.push(message);
    })
  }
};
</script>

<style></style>
