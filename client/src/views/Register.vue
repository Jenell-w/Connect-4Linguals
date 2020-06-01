<template>
  <div>
    <navBar/>
    <h1>Register</h1>
    <!-- Pete, work your magic! Can you make login boxes disappear after user is logged in? -->
    <form>
      <label for="username">Enter your username:</label>
      <input type="user" id="user" />
      <br />
      <br />
      <label for="pswd">Enter your password:</label>
      <input type="password" id="pswd" />
      <br />
      <br />
      <input type="button" value="Submit" />
    </form>
  </div>
</template>

<script>
import navBar from "../components/navBar"

export default {
  name: "App",
    components: {
    navBar
  }
};
</script>

<style></style>