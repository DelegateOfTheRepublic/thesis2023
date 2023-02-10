<template>
  <div id="app">
    <navbar/>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'app',
  components: {
    Navbar
  }
}
</script>

<style scoped>
#app{
  min-height: inherit;
}

.container{
  margin-top: 80px;
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
}
</style>
