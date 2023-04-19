<template>
<div class="day_week">
    <p>{{week[day_number-1]}}</p>
    <p>{{date}}</p>
</div>
</template>

<script>
export default {
    props: ['day_number'],
    data() {
        return {
            week: ['Пн.', 'Вт.', 'Ср.', 'Чт.', 'Пт.', 'Сб.'],
            date: '16.03.23'
        }
    }
}
</script>

<style scoped>
p{
    margin: 0px;
    width: fit-content;
    margin: auto;
}

.day_week{
    padding: 5px;
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}
</style>