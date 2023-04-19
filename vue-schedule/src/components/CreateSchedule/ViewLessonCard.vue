<template>
<div class="lesson-card-wrapper" :class="{ 'lesson-card-wrapper--reverse': isTopStats }">
    <div class="view_card">
        <div v-if="withTitle" class="view_card__title">
            <p>{{lesson_number}}-я пара</p>
            <p>{{lesson_time.start}}-{{lesson_time.end}}</p>
        </div>
        <div class="view_card__wrapper">
            <div class="view_card__info">
                <icon-label icon_name="icon-subject" font_size="19">
                    <p>{{subject}}</p>
                </icon-label>
                <icon-label icon_name="icon-teacher" font_size="19">
                    <p>{{teacher.position}} {{teacher.name}}</p>
                </icon-label>
                <icon-label icon_name='icon-location' font_size='19'>
                    <p>Ауд. {{auditorium}}</p>
                </icon-label>
                <icon-label icon_name="icon-calendar" font_size="19">
                    <p>С {{lesson_dates.start}}-{{lesson_dates.end}} н.</p>
                </icon-label>
            </div>
            <div class="view_card__add_info">
                <icon icon_name="icon-online_lesson" font_size="30"></icon>
                <icon icon_name="icon-lecture" font_size="30"></icon>
                <icon icon_name="icon-practice" font_size="30"></icon>
                <icon icon_name="icon-groups" font_size="30"></icon>
            </div>
        </div>
        <slider v-if="slider"/>
    </div>
    <div v-if="withStats" class="view_card__stats" :class="{ 'view_card__stats--top': isTopStats }">
        <icon icon_name="icon-close" font_size="19"/>
        <icon icon_name="icon-edit" font_size="19"/>
        <icon icon_name="icon-duplicated" font_size="19"></icon>
        <icon icon_name="icon-linking" font_size="19"></icon>
        <icon icon_name="icon-main" font_size="19"></icon>
        <icon icon_name="icon-go_to" font_size="19"/>
        <icon icon_name="icon-unlink" font_size="19"/>
        <icon icon_name="icon-set_name" font_size="19"/>
    </div>
</div>
</template>

<script>
import IconLabel from '../IconLabel.vue'
import Slider from '../Slider.vue'

export default {
    props: {
        withTitle: {
            type: Boolean,
            default: true
        },
        isTopStats: {
            type: Boolean,
            default: false
        },
        withStats: {
            type: Boolean,
            default: true
        },
        slider: {
            type: Boolean,
            default: true
        }
    },
    components:{
        Slider,
        IconLabel
    },
    data(){
        return{
            lesson_number: 1,
            lesson_time: {
                'start': '8:30',
                'end': '9:50'
            },
            subject: 'Нейроинформатика',
            teacher: {
                'position': 'Доц.',
                'name': 'Полупанов Д.В.'
            },
            auditorium: 525,
            lesson_dates: {
                'start': '27',
                'end': '31'
            }
        }
    }
}
</script>

<style scoped>
p {
    margin: 0;
}
.lesson-card-wrapper {
    display: flex;
    gap: 12px;
}
.lesson-card-wrapper--reverse {
    flex-direction: column-reverse;
}
.view_card {
    height:fit-content;
    display: flex;
    position: relative;
    flex-direction: column;
    gap: 5px;
    background-color: bisque;
}

.view_card__wrapper {
    background-color: cadetblue;
}

.view_card__title {
    display: flex;
    justify-content: space-between;
}

.view_card__info {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.view_card__add_info {
    display: flex;
    width: fit-content;
    margin: 5px auto 0px;
    gap: 10px;
}

.view_card__stats {
    display: flex;
    flex-direction: column;
    gap: 5px;
}
.view_card__stats--top {
    flex-direction: row-reverse;
}
</style>