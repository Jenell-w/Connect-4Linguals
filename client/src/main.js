import Vue from "vue";
import App from "./App.vue";
import router from "./router";
//import socketio from "socket.io";
//import VueSocketIO from "vue-socket.io";

Vue.config.productionTip = false;

export const globalSessionVar = new Vue();
//export const SocketInstance = socketio("http://127.0.0.1:5000/");
//Vue.use(VueSocketIO, SocketInstance);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
