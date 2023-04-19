<template>
<div class="to-duplicate">
    <view-lesson-card :withTitle="false" :is-top-stats="true" v-for="i in 4" :key="i"/>
    <edit-lesson-card :with-title="false"/>
</div>
</template>

<script>
import EditLessonCard from './EditLessonCard.vue'
import ViewLessonCard from './ViewLessonCard.vue'
export default {
  components: { ViewLessonCard, EditLessonCard },

}
</script>

<style scoped>
.to-duplicate {
    display: flex;
    gap: 30px;
}
</style>