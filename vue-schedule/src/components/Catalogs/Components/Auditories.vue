<template>
    <div class="audit-catalog">
        <div class="audit-catalog__head">
            <span>Аудитории</span>
            <v-button :iconName="'icon-add'" :fontSize="15"/>
        </div>
        <div class="audit-catalog__add-audit">
            <div class="add-audit__select">
                <span>Факультет:</span>
                <select name="" id="">
                    <option value="">ФМиИТ</option>
                </select>
            </div>
            <div class="add-audit__input">
                <span>Номер:</span>
                <input type="text" placeholder="..."/>
            </div>
            <div class="add-audit__audit-type">
                <v-button :iconName="'icon-computer'" :fontSize="22"/>
                <v-button :iconName="'icon-projector'" :fontSize="22"/>
            </div>
            <div class="add-audit__submition">
                <v-button :iconName="'icon-submit'" :fontSize="15" :title="'Добавить'"/>
                <v-button :iconName="'icon-cancel'" :fontSize="15" :title="'Отмена'"/>
            </div>
        </div>
        <search-bar/>
        <div class="audit-catalog__list">
            <div class="audit-catalog__list-item" v-for="i in 3" :key="i">
                <icon-label :icon_name="'icon-door'" :font_size="22">524</icon-label>
                <div class="list-item__stats">
                    <icon icon_name="icon-computer" font_size="22"/>
                    <icon icon_name="icon-projector" font_size="22"/>
                </div>
            </div>
        </div>
        <pagination/>
    </div>
</template>

<script>
import Icon from '../../Icon.vue';
import IconLabel from '../../IconLabel.vue';
import VButton from '../../VButton.vue';
import Pagination from '../../Pagination.vue';
import SearchBar from '../../SearchBar.vue';

export default {
    components: {
        Icon, IconLabel, VButton, Pagination,
        SearchBar
    },
    data() {
        return {

        }
    }
}
</script>

<style scoped>
.audit-catalog {
    width: 200px;
    height: fit-content;

    background-color: bisque;
}
.audit-catalog__head {
    display: flex;
    justify-content: space-between;
    align-items: center;

    background-color: cornflowerblue;
}
.audit-catalog__list {
    margin-top: 10px;

    background-color: cornflowerblue;
}
.audit-catalog__list-item {
    display: flex;
    justify-content: space-between;
}
.list-item__stats {
    display: flex;
    align-items: center;
    gap: 8px;
}
.audit-catalog__add-audit {
    display: none;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.audit-catalog__head:hover + .audit-catalog__add-audit {
    display: block;
}
.add-audit__input {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 6px;
}
.add-audit__input>input {
    width: 95%;
}
.add-audit__audit-type {
    width: fit-content;
    display: flex;
    gap: 25px;
    margin: 6px auto 0;
}
.add-audit__submition {
    display: flex;
    justify-content: space-between;
    margin-top: 12px;
}
</style>