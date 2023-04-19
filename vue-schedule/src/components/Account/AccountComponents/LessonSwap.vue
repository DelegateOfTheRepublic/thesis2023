<template>
    <div class="lesson-swap">
        <div class="lesson-swap__date">
            <v-button :iconName="'icon-arrow_left'" :fontSize="12"/>
            <span>{{ currentDate }}</span>
            <v-button :iconName="'icon-arrow_right'" :fontSize="12"/>
        </div>
        <div class="lesson-swap__menu">
            <div class="lesson-swap__item" v-for="i in 2" :key="i">
                <div class="lesson-swap__item-title">
                    <span>1-я пара</span>
                    <span>13:40-15:00</span>
                </div>
                <div class="lesson-swap__item-content">
                    <span>доц. Абдюшева С.Р.</span>
                    <span>Теория игр и исследование операций</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import VButton from '../../VButton.vue';

export default {
    components: {
        VButton
    },
    data() {
        return {
            currentDate: '06.03.23'
        }
    }
}
</script>

<style scoped>
.lesson-swap {
    background-color: bisque;
}
.lesson-swap__date {
    width: fit-content;
    display: flex;
    gap: 4px;
    align-items: center;
    margin: 0 auto 20px;
}
.lesson-swap__menu {
    display: flex;
    flex-direction: column;
    gap: 15px;
}
.lesson-swap__item,
.lesson-swap__item-content {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.lesson-swap__item {
    background-color: cornflowerblue;
}
.lesson-swap__item-title {
    display: flex;
    justify-content: space-between;
}
.lesson-swap__item-content {
    max-width: 180px;
    gap: 6px;
    text-align: center;
}
</style>