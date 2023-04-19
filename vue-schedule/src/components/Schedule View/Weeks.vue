<template>
<div class="week">
    <div class="week__info">
        <p>Текущая неделя: {{current_type_week}}</p>
        <p>По счету: {{week_number}}-я</p>
    </div>
    <div class="week__days">
        <day-week v-for="i in 6" :key="i" :day_number="i"/>
    </div>
</div>
</template>

<script>
import DayWeek from '../DayWeek.vue'
export default {
  components: { DayWeek },
    data(){
        return {
            current_type_week: 'верхняя',
            week_number: '20'
        }
    }
}
</script>

<style scoped>

.week {
    width: 640px;
    padding: 5px;
    background-color:bisque;
}

.week__info {
    width: 60%;
    display: flex;
    justify-content: space-between;
    margin: auto;
}

.week__days {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
}
</style>