<template>
    <!-- <person-info/> -->
    <!-- <my-groups/> -->
    <!-- <my-links/> -->
    <!-- <group-list/> -->
    <lesson-detail/>
    <!-- <lesson-swap/> -->
</template>

<script>
import GroupList from './AccountComponents/GroupList.vue'
import LessonDetail from './AccountComponents/LessonDetail.vue'
import MyGroups from './AccountComponents/MyGroups.vue'
import MyLinks from './AccountComponents/MyLinks.vue'
import PersonInfo from './AccountComponents/PersonInfo.vue'
import LessonSwap from './AccountComponents/LessonSwap.vue'

export default {
  components: { PersonInfo, MyGroups, MyLinks, GroupList, LessonDetail, LessonSwap },

}
</script>

<style scoped>

</style>