<template>
  <div id="app">
    <navbar/>
    <!-- <create-schedule/> -->
    <!-- <account/> -->
    <catalogs-page/>
  </div>
</template>

<script>
import Account from './components/Account/Account.vue'
import CreateSchedule from './components/CreateSchedule.vue'
import Navbar from './components/Navbar.vue'
import ScheduleView from './components/ScheduleView.vue'
import CatalogsPage from './components/Catalogs/CatalogsPage.vue'

export default {
  name: 'app',
  components: {
    Navbar,
    ScheduleView,
    CreateSchedule,
    Account,
    CatalogsPage
  }
}
</script>

<style scoped>
#app{
  display: flex;
  flex-direction: column;
  min-height: inherit;
}
</style>
