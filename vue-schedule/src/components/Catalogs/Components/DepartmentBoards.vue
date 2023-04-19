<template>
    <div class="department-boards">
        <div class="dept-boards__head">
            <span>Кафедры</span>
            <v-button :iconName="'icon-add'" :fontSize="15"/>
        </div>
        <div class="dept-boards__add-dept_board">
            <div class="add-dept_board__dept-select">
                <span>Факультет:</span>
                <select name="" id="">
                    <option value="">ФМиИТ</option>
                </select>
            </div>
            <div class="add-dept_board__input">
                <span>Номер:</span>
                <input type="text" placeholder="..."/>
            </div>
            <div class="add-dept_board__submition">
                <v-button :iconName="'icon-submit'" :fontSize="15" :title="'Добавить'"/>
                <v-button :iconName="'icon-cancel'" :fontSize="15" :title="'Отмена'"/>
            </div>
        </div>
        <div class="dept-boards__dept-select">
            <span>Факультет:</span>
            <select name="" id="">
                <option value="">ФМиИТ</option>
            </select>
        </div>
        <div class="dept-boards__list">
            <div class="dept-boards__list-item">
                <span>{{ deptBoards.a }}</span>
                <icon-label :icon_name="'icon-door'" :font_size="22">520</icon-label>
            </div>
            <div class="dept-boards__list-item">
                <span>{{ deptBoards.b }}</span>
                <icon-label :icon_name="'icon-door'" :font_size="22">523a, 514a</icon-label>
            </div>
        </div>
    </div>
</template>

<script>
import IconLabel from '../../IconLabel.vue';
import VButton from '../../VButton.vue';

export default {
    components: { IconLabel, VButton },
    data() {
        return {
            deptBoards: {
                'a': 'Кафедра информационных технологий и компьютерной математики',
                'b': 'Кафедра программирования и экономической информатики'
            }
        }
    }
}
</script>

<style scoped>
.department-boards {
    width: 260px;

    background-color: bisque;
}
.dept-boards__head {
    display: flex;
    justify-content: space-between;
    align-items: center;

    background-color: cornflowerblue;
}
.dept-boards__dept-select {
    width: fit-content;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.dept-boards__dept-select>select {
    margin-left: 6px;
}
.dept-boards__list {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.dept-boards__list-item {
    background-color: cornflowerblue;
}

.dept-boards__add-dept_board {
    display: none;

    background-color: cornflowerblue;
}
.dept-boards__head:hover + .dept-boards__add-dept_board {
    display: block;
}
.add-dept_board__input {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 6px;
}
.add-dept_board__input>input {
    width: 95%;
}
.add-dept_board__submition {
    display: flex;
    justify-content: space-between;
    margin-top: 12px;
}
.add-dept_board__dept-select {
    width: fit-content;
    margin-top: 10px;
}
</style>