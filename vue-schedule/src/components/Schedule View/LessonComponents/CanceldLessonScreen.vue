<template>
<div class="canceld_lesson">
    <icon icon_name="icon-arrow_back" font_size='15'></icon>
    <p>На сегодня пара отменена</p>
    <p>Причина: {{reason}}</p>
</div>
</template>

<script>
export default {
    data(){
        return{
            reason: 'не указана'
        }
    }
}
</script>

<style scoped>
p{
    margin: 0;
}

.canceld_lesson{
    width: 100%;
    height: 100%;
}

.canceld_lesson>div{
    margin-bottom: 10px;
}
</style>