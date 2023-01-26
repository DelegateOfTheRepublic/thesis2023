<template>
    <div>
        <navbar/>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script>
import Navbar from './Navbar.vue'

export default {
components: {
    Navbar
  }
}
</script>

<style scoped>
.container{
  margin-top: 80px;
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
}
</style>