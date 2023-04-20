<template>
<div class="edit-card">
    <div v-if="withTitle" class="edit-card__title">
        <p>{{lessonNumber}}-я пара</p>
        <p>{{lessonTime.start}}-{{lessonTime.end}}</p>
    </div>
    <div class="edit-card__wrapper">
        <div class="edit-card__info">
            <div>
                <p>Дисциплина:</p>
                <select name="" id="">
                    <option selected disabled hidden></option>
                    <option value="">{{subject}}</option>
                </select>
            </div>
            <div>
                <p>Преподаватель:</p>
                <select name="" id="">
                    <option selected disabled hidden></option>
                    <option value="">{{teacher}}</option>
                </select>
            </div>
            <div class="edit-card__auditorium">
                <p>Аудитория:</p>
                <div>
                    <p>{{auditorium}}</p>
                    <icon icon_name="icon-cancel" font_size="10"></icon>
                </div>
                <icon icon_name="icon-add" font_size="12"></icon>
            </div>
            <div class="edit-card__dates">
                <div>
                    <p>С:</p>
                    <select name="" id="">
                        <option selected disabled hidden></option>
                        <option value="">{{dates.start}}</option>
                    </select>
                </div>
                <div>
                    <p>По:</p>
                    <select name="" id="">
                        <option selected disabled hidden></option>
                        <option value="">{{dates.end}}</option>
                    </select>
                </div>
            </div>
            <div>
                <p>Тип занятия:</p>
                <select name="" id="">{{lessonType}}</select>
            </div>
        </div>
        <div class="edit-card__add-info">
            <icon icon_name="icon-online_lesson" font_size="25"></icon>
            <icon icon_name="icon-groups" font_size="25"></icon>
            <icon icon_name="icon-separation" font_size="25"></icon>
        </div>
    </div>
    <div class="edit-card__btns">
        <v-button :title="'Сохранить'" :iconName="'icon-save'" :fontSize="16"/>
        <v-button :title="'Отменить'" :iconName="'icon-cancel'" :fontSize="14"/>
    </div>
    <slider/>
</div>
</template>

<script>
import Icon from '../Icon.vue'
import vButton from '../VButton.vue'
import Slider from '../Slider.vue'

export default {
    props: {
        withTitle: {
            type: Boolean,
            default: true
        }
    },
    components: {
        Icon,
        Slider,
        'v-button': vButton
    },
    data() {
        return {
            lessonNumber: 1,
            lessonTime: {
                'start': '10:05',
                'end': '11:25'
            },
            subject: 'Нейроинформатика',
            teacher: 'Антон В.Б.',
            auditorium: 521,
            dates: {
                'start': '27',
                'end': '31'
            },
            lessonType: 'Лекция'
        }
    }
}
</script>

<style scoped>
.edit-card {
    width: fit-content;
    display: flex;
    flex-direction: column;
    gap: 15px;
    background-color: bisque;
}

.edit-card__title {
    display: flex;
    justify-content: space-between;
}

.edit-card__wrapper {

}

.edit-card__info {
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: cadetblue;
}

.edit-card__info>div:has(select) {
    display: flex;
    align-items: center;
    gap: 5px;
}

.edit-card__auditorium {
    display: flex;
    gap: 5px;
    align-items: center;
}

.edit-card__auditorium>div {
    display: flex;
    align-items: center;
    gap: 5px;
}

.edit-card__auditorium>div[name='icon'] {
    margin-left: 10px;
}

.edit-card__dates {
    display: flex;
    gap: 25px;
}

.edit-card__dates>div {
    display: flex;
    gap: 5px;
    align-items: center;
}

.edit-card__add-info {
    width: fit-content;
    display: flex;
    gap: 25px;
    margin: 15px auto 0px;
}

.edit-card__btns {
    display: flex;
    gap: 20px;
    margin: auto;
}

p {
    margin: 0;
}
</style>