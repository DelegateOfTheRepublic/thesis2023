<template>
    <div class="lesson-detail">
        <span>{{ subject }}</span>
        <v-button :iconName="'icon-close'" :fontSize="18"/>
        <div class="lesson-detail__info">
            <span>Номер пары: {{ lessonNumber }}</span>
            <span>Время: {{ lessonTime.start }}-{{ lessonTime.end }}</span>
            <span>Аудитория: {{ auditorium }}</span>
            <span>Даты: {{ lessonDates.start }}-{{ lessonDates.end }} н.</span>
            <span>Группы: {{ additGroups }}</span>
            <div class="lesson-detail__stats">
                <span>Статусы</span>
                <div class="lesson-detail__wrapper">
                    <v-button :iconName="'icon-swap_lesson'" :fontSize="18"/>
                    <v-button :iconName="'icon-lesson_canceld'" :fontSize="18"/>
                    <v-button :iconName="'icon-late'" :fontSize="18"/>
                    <v-button :iconName="'icon-time_shift'" :fontSize="18"/>
                    <v-button :iconName="'icon-change_audit'" :fontSize="18"/>
                    <v-button :iconName="'icon-homework'" :fontSize="18"/>
                    <v-button :iconName="'icon-online_lesson'" :fontSize="18"/>
                </div>
            </div>
        </div>
        <div class="lesson-detail__toolbar">
            <v-button :iconName="'icon-swap_lesson'" :fontSize="22"/>
            <v-button :iconName="'icon-lesson_canceld'" :fontSize="22"/>
            <v-button :iconName="'icon-late'" :fontSize="22"/>
            <v-button :iconName="'icon-time_shift'" :fontSize="22"/>
            <v-button :iconName="'icon-change_audit'" :fontSize="22"/>
            <v-button :iconName="'icon-homework'" :fontSize="22"/>
            <v-button :iconName="'icon-online_lesson'" :fontSize="22"/>
        </div>
    </div>
</template>

<script>
import VButton from '../../VButton.vue'

export default {
    components: {
        VButton
    },
    data() {
        return {
            subject: 'Нейроинформатика',
            lessonNumber: '1',
            lessonTime: {
                'start': '13:40',
                'end': '15:00'
            },
            auditorium: '525',
            lessonDates: {
                'start': '22',
                'end': '25'
            },
            additGroups: '41, 46'
        }
    }
}
</script>

<style scoped>
.lesson-detail {
    display: grid;
    grid-template-columns: 1fr auto;
    row-gap: 10px;
    column-gap: 10px;
    align-items: center;
    width: fit-content;

    background-color: bisque;
}
.lesson-detail>div[id=v-button] {
    justify-self: center;
}
.lesson-detail__head {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.lesson-detail__content {
    display: flex;
    gap: 20px;
    margin-top: 15px;
}
.lesson-detail__info {
    display: flex;
    flex-direction: column;
    gap: 6px;

    background-color: cornflowerblue;
}
.lesson-detail__toolbar {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    background-color: cornflowerblue;
}
.lesson-detail__stats {

}
.lesson-detail__stats--no-stats {
    text-align: center;
    margin-top: 10px;
}
.lesson-detail__wrapper {
    width: min-content;
    display: grid;
    grid-template-columns: repeat(5, auto);
    row-gap: 5px;
    column-gap: 10px;
    margin: auto;
    margin-top: 10px;

    background-color: crimson;
}
</style>