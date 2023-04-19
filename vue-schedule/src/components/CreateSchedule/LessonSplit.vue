<template>
    <div class="lesson-split">
        <span>Разделение пары</span>
        <div class="lesson-split__week-type">
            <v-button :iconName="'icon-radio-checked'" :fontSize="15" :title="'Верхняя неделя'"/>
            <v-button :iconName="'icon-radio-checked'" :fontSize="15" :title="'Нижняя неделя'"/>
        </div>
        <div class="lesson-split__btns">
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
.lesson-split {
    display: flex;
    flex-direction: column;
    gap: 10px;
    background-color: bisque;
}
.lesson-split__week-type {
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.lesson-split__btns {
    display: flex;
    gap: 40px;
    margin: auto;
}
</style>