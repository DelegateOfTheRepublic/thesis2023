<template>
    <div class="person-info">
        <div class="person-info__head">
            <icon icon_name="icon-avatar" font_size="80"/>
            <div class="person-info__contacts">
                <span>{{ fio }}</span>
                <div class="person-info__wrapper">
                    <icon-label :icon_name="'icon-telephone'" :font_size="22">{{ telephone }}</icon-label>
                    <icon-label :icon_name="'icon-email'" :font_size="22">{{ email }}</icon-label>
                </div>
            </div>
        </div>
        <div class="person-info__work-info">
            <span>Рабочая информация</span>
            <div class="person-info__wrapper">
                <span>Должность: {{ position }}</span>
                <span>Факультет: {{ department }}</span>
                <span>Направление: {{ specialization }}</span>
                <span>Кафедра: {{ departmentBoard }}</span>
                <span>Курс: {{ course }}</span>
                <span>Группа: {{ studyGroup }}</span>
            </div>
        </div>
        <div class="person-info__group-contacts">
            <span>Связь с группой</span>
            <span>Email: {{ groupEmail }}</span>
        </div>
    </div>
</template>

<script>
import Icon from '../../Icon.vue'
import IconLabel from '../../IconLabel.vue'

export default {
    components: {
        Icon, IconLabel
    },
    data() {
        return {
            fio: 'Антон Васильев Бобич',
            telephone: '+7 (999) 888-98-57',
            email: 'myemail@mail.ru',
            position: 'Студент',
            department: 'Факультет математики и иформационных технологий',
            specialization: 'Прикладная информатика',
            departmentBoard: 'Информационные и вычислительные технологии',
            course: '4',
            studyGroup: 'ПИ-4ИВТ186А',
            groupEmail: 'group_email@mail.ru'
        }
    }
}
</script>

<style scoped>
.person-info {
    display: flex;
    flex-direction: column;
    gap: 50px;
    background-color: bisque;
}
.person-info__head {
    width: fit-content;
    display: flex;
    align-items: center;
    gap: 20px;
    background-color: cornflowerblue;
}
.person-info__contacts {

}
.person-info__wrapper {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}
.person-info__work-info {
    background-color: cornflowerblue;
}
.person-info__group-contacts {
    width: fit-content;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: cornflowerblue;
}
</style>