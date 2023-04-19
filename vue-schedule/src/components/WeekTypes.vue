<template>
<div class="week_types">
    <div class="week_types__up">
        <p>Нижние недели</p>
        <div v-for="i in 8" :key="i">
            <p>{{week_number}}-я неделя</p>
            <p>{{week_dates}}</p>
        </div>
    </div>
    <div class="week_types__down">
        <p>Верхние недели</p>
        <div v-for="i in 9" :key="i">
            <p>{{week_number}}-я неделя</p>
            <p>{{week_dates}}</p>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{
            week_number: '20',
            week_dates: '06.02-11.02'
        }
    }
}
</script>

<style scoped>

.week_types {
    width: fit-content;
    display: flex;
    gap: 40px;
    padding: 15px;
    background-color:bisque;
}

.week_types__up,
.week_types__down {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
}

.week_types__up>div,
.week_types__down>div{
    width: fit-content;
}
</style>