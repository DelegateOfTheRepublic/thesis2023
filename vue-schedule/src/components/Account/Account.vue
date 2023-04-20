<template>
  <div class="content">
    <div class="content__left">

    </div>
    <div class="content__middle content--flex">
      <person-info/>
      <div class="account__section-my">
        <my-groups/>
        <my-links/>
      </div>
    </div>
    <div class="content__right">
      <group-list/>
    </div>
  </div>
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
.account__section-my {
  height: fit-content;
  display: inline-flex;
  flex-direction: column;
  gap: 70px;
  margin-left: auto;
}
</style>