<template>
  <div id="app">
    <GameBoard title="Play Connect 4 Linguals" />
  </div>
</template>

<script>
import GameBoard from "../components/GameBoard";
import { isAuthenticated } from './helpers';


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
  }
};
</script>

<style></style>
