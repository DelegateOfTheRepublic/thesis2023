<template>
<div class="new-schedule">
    <div class="new-schedule-top">
        <div class="new-schedule__schedule-type">
            <span>Расписание:</span>
            <select name="" id="">
                <option selected value="">учебное</option>
            </select>
        </div>
        <div class="new-schedule__study-group">
            <span>Группа:</span>
            <select name="" id="">
                <option value="">ПИ-4ИВТ186А</option>
            </select>
        </div>
    </div>
    <div class="new-schedule-bottom">
        <v-button :iconName="'icon-checkbox'" :fontSize="17" :title="'вкл. дублирование'"/>
        <div class="new-schedule__study-group">
            <span>Группа:</span>
            <select name="" id="">
                <option value="">ПИ-4ИВТ186А</option>
            </select>
        </div>
        <div class="new-schedule__study-days">
            <span>Учебные дни</span>
            <div class="study-days">
                <day-week v-for="i in 6" :key="i" :day_number="i" :noDate="true"/>
            </div>
        </div>
        <div class="new-schedule__lesson-nums">
            <span>Номера пар</span>
            <div class="lesson-nums">
                <span v-for="i in 6" :key="i">{{ i }}</span>
            </div>
        </div>
        <div class="new-schedule__selection-info">
            <v-button :iconName="'icon-checkbox'" :fontSize="17" :title="'6 элементов'"/>
            <span class="selection-info__btns">
                <v-button :iconName="'icon-duplicate'" :fontSize="17"/>
                <v-button :iconName="'icon-linking'" :fontSize="17"/>
            </span>
        </div>
    </div>
</div>
</template>

<script>
import DayWeek from '../DayWeek.vue'
import VButton from '../VButton.vue'
export default {
    components: {
        VButton,
        DayWeek,
    }
}
</script>

<style scoped>
.new-schedule {
    background-color: bisque;
}
.new-schedule-top {
    background-color: cadetblue;
    margin-bottom: 16px;
}
.new-schedule__schedule-type {
    margin-bottom: 8px;
}
.new-schedule__study-group {

}
.new-schedule-bottom {
    display: flex;
    flex-direction: column;
    gap: 8px;
    background-color: cadetblue;
}
.new-schedule__study-days {

}
.study-days,
.lesson-nums {
    display: flex;
    gap: 10px;
}
.new-schedule__lesson-nums {

}
.new-schedule__selection-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.selection-info__btns {
    display: flex;
}
</style>