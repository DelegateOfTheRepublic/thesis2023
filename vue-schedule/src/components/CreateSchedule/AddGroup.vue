<template>
    <div class="add-group">
        <span>Добавить группу</span>
        <div class="add-group__content">
            <div class="add-group__current-groups">
                <span>ПИ-4ИВТ176А</span>
                <span>ПИ-4ИВТ176А</span>
            </div>
            <div class="separator"></div>
            <div class="add-group__groups-list">
                <span>ПИ-4ИВТ176А</span>
                <span>ПИ-4ИВТ176А</span>
                <span>ПИ-4ИВТ176А</span>
                <span>ПИ-4ИВТ176А</span>
            </div>
        </div>
        <div class="add-group__btns">
            <v-button :iconName="'icon-submit'" :fontSize="16"/>
            <v-button :iconName="'icon-cancel'" :fontSize="16"/>
        </div>
    </div>
</template>

<script>
import VButton from '../VButton.vue'

export default {
    components: {
        VButton
    }
}
</script>

<style scoped>
.add-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    background-color: bisque;
}
.add-group__content {
    width: min-content;
}
.add-group__current-groups, .add-group__groups-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
    width: min-content;
    background-color: cadetblue;

}
.add-group__current-groups {

}
.separator {
    margin: 5px 0;
    border: 2px dashed #000000;
}
.add-group__groups-list {

}
.add-group__btns {
    display: flex;
    gap: 40px;
}
</style>