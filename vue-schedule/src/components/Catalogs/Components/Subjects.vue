<template>
    <div class="subjects">
        <div class="subjects__head">
            <span>Дисциплины</span>
            <v-button :iconName="'icon-add'" :fontSize="15"/>
        </div>
        <div class="subjects__add-subject">
            <div class="add-subject__input">
                <icon icon_name="icon-subject" font_size="22"/>
                <input type="text" placeholder="Наименование..."/>
            </div>
            <div class="add-subject__submition">
                <v-button :iconName="'icon-submit'" :fontSize="15" :title="'Добавить'"/>
                <v-button :iconName="'icon-cancel'" :fontSize="15" :title="'Отмена'"/>
            </div>
        </div>
        <search-bar :department-select="false"/>
        <div class="subjects__list">
            <icon-label :icon_name="'icon-subject'" :font_size="22" v-for="i in 2" :key="i">
                Нейроинформатика
            </icon-label>
            <icon-label :icon_name="'icon-subject'" :font_size="22" v-for="i in 2" :key="i">
                Основы проектной деятельности
            </icon-label>
        </div>
        <pagination/>
    </div>
</template>

<script>
import Icon from '../../Icon.vue'
import IconLabel from '../../IconLabel.vue'
import Pagination from '../../Pagination.vue'
import SearchBar from '../../SearchBar.vue'
import VButton from '../../VButton.vue'
export default {
  components: { Pagination, SearchBar, VButton, IconLabel, Icon },

}
</script>

<style scoped>
.subjects {
    max-width: 220px;
    height: fit-content;

    background-color: bisque;
}
.subjects__head {
    display: flex;
    justify-content: space-between;
    align-items: center;

    background-color: cornflowerblue;
}
.subjects__list {
    margin-top: 10px;

    background-color: cornflowerblue;
}
.subjects__add-subject {
    display: none;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.add-subject__input {
    display: flex;
    align-items: center;
    gap: 6px;
}
.add-subject__submition {
    display: flex;
    justify-content: space-between;
    margin-top: 12px;
}
.add-subject__input>input {
    width: 100%;
}
.subjects__head:hover + .subjects__add-subject {
    display: block;
}
</style>