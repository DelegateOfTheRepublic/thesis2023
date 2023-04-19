<template>
    <div class="st-groups">
        <div class="st-groups__head">
            <span>Учебные группы</span>
            <div class="st-groups__head-btns">
                <v-button :iconName="'icon-add'" :fontSize="15"/>
                <v-button :iconName="'icon-params'" :fontSize="19"/>
            </div>
        </div>
        <div class="st-group__add-st-group">
            <div class="add-st-group__input">
                <span>Номер:</span>
                <input type="text" placeholder="..."/>
            </div>
            <div class="add-st-group__submition">
                <v-button :iconName="'icon-submit'" :fontSize="15" :title="'Добавить'"/>
                <v-button :iconName="'icon-cancel'" :fontSize="15" :title="'Отмена'"/>
            </div>
        </div>
        <div class="st-group__filter">
            <select name="" id="">
                <option disabled selected value="">Высшее образование</option>
                <option value="">Бакалавриат</option>
            </select><select name="" id="">
                <option disabled selected value="">Направление подготовки</option>
                <option value="">ПИ</option>
            </select><select name="" id="">
                <option disabled selected value="">Курс</option>
                <option value="">4</option>
            </select>
        </div>
        <div class="st-groups__list">
            <icon-label :icon_name="'icon-group'" :font_size="22" v-for="i in 5" :key="i">ПИ-4ИВТ186А</icon-label>
        </div>
    </div>
</template>

<script>
import IconLabel from '../../IconLabel.vue'
import VButton from '../../VButton.vue'
export default {
  components: { VButton, IconLabel },

}
</script>

<style scoped>
.st-groups {
    width: 250px;
    height: fit-content;

    background-color: bisque;
}
.st-groups__head {
    display: flex;
    justify-content: space-between;

    background-color: cornflowerblue;
}
.st-groups__head-btns {
    display: flex;
    align-items: center;
    gap: 12px;
}
.st-group__add-st-group {
    display: none;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.add-st-group__input {
    display: flex;
    gap: 6px;
    align-items: center;
}
.add-st-group__input>input {
    width: 100%;
}
.add-st-group__submition {
    display: flex;
    justify-content: space-between;
    margin-top: 12px;
}
.st-groups__list {
    margin-top: 10px;

    background-color: cornflowerblue;
}
.st-groups__head:hover + .st-group__add-st-group {
    display: block;
}
.st-group__filter {
    display: none;
    flex-direction: column;
    gap: 6px;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.st-groups__head:hover + .st-group__filter {
    display: flex;
}
</style>