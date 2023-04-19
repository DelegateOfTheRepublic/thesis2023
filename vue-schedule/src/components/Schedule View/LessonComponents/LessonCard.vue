<template>
<div class="lesson">
    <div class="lesson__title">
        <p>{{lesson_number}}</p>
        <p>{{time_interval}}</p>
    </div>
    <div class="lesson__content">
        <div class="lesson__info">
            <div class="subject">
                <p>{{subject}}</p>
            </div>
            <div class="lesson__location">
                <icon icon_name="icon-location"></icon>
                <p>{{auditorium}}</p>
            </div>
            <div class="lesson__dates">
                <icon icon_name="icon-calendar"></icon>
                <p>{{dates}}</p>
            </div>
            <div class="lesson__teacher">
                <icon icon_name="icon-teacher"></icon>
                <p>{{teacher}}</p>
            </div>
            <!--<late-screen/>-->
            <!--<online-lesson-screen/>-->
            <!--<homework-screen/>-->
            <!--<canceld-lesson-screen/>-->
        </div>
        <div class="lesson__statuses">
            <icon icon_name="icon-late" :font_size='status_icon_size'></icon>
            <icon icon_name="icon-online_lesson" :font_size='status_icon_size'></icon>
            <icon icon_name="icon-homework" :font_size='status_icon_size'></icon>
            <icon icon_name="icon-lesson_canceld" :font_size='status_icon_size'></icon>
        </div>
        <p class="lesson__type">{{lesson_type}}</p>
        <icon icon_name="icon-completed" :font_size='status_icon_size'></icon>
    </div>
    <div class="lesson__time_bar">
        <div class="time_bar__progress"></div>
        <p>{{current_time}}</p>
    </div>
    <slider/>
</div>
</template>

<script>
import Icon from '../../Icon.vue'
import Slider from '../../Slider.vue'
import LateScreen from '../LessonComponents/LateScreen.vue'
import CanceldLessonScreen from './CanceldLessonScreen.vue'
import HomeworkScreen from './HomeworkScreen.vue'
import OnlineLessonScreen from './OnlineLessonScreen.vue'

export default {
  components: { Slider, LateScreen, OnlineLessonScreen, HomeworkScreen, CanceldLessonScreen, Icon},
    data(){
        return {
            status_icon_size: 30,
            lesson_number: '1-я пара',
            time_interval: '8:30-10:05',
            subject: 'Теория игр и исследование операцийasdasdasdafasefasghshgasjkghkjsadfgjkasghjksh',
            auditorium: 'Ауд. 530',
            dates: 'По 22-25 н.',
            teacher: 'Доц. Ишмухаметов Н.С.',
            lesson_type: 'Практика',
            current_time: '01:20'
        }
    }
}
</script>

<style scoped>
p{
    margin: 0px;
}
</style>