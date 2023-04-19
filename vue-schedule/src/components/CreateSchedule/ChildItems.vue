<template>
<div class="child-items">
    <span>Дочерние элементы</span>
    <div class="child-list">
        <view-lesson-card v-for="i in 3" :key="i"/>
    </div>
</div>
</template>

<script>
import ViewLessonCard from './ViewLessonCard.vue'
export default {
    components: {
        ViewLessonCard,
    }
}
</script>

<style scoped>
.child-items {
    background-color:aquamarine;
}
.child-items>span {
    display: block;
    text-align: center;
}
.child-list {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}
</style>