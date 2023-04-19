<template>
    <component :submitCreateStDay='submitCreateStDay' :is="currentLessonComponent" @click="swithLessonComponent"/>
</template>

<script>
import LessonCreater from './LessonCreater.vue'
import AddLesson from './AddLesson.vue'
export default {
  components: {
        LessonCreater,
        AddLesson,
  },
  props: ['submitCreateStDay'],
  data() {
      return {
          currentLessonComponent: AddLesson
      }
  },
  methods: {
      swithLessonComponent: function() {
          if (this.currentLessonComponent === AddLesson){
              this.currentLessonComponent = LessonCreater
          }else{
              this.currentLessonComponent = AddLesson
          }
      }
  }
}
</script>