<template>
<div class="late_screen">
    <icon icon_name="icon-arrow_back" font_size='15'></icon>
    <p>Преподаватель задерживается</p>
    <p>Причина: {{reason}}</p>
    <p>Время ожидания: {{waiting_time}} мин.</p>
</div>
</template>

<script>
export default {
    data(){
        return{
            reason: 'не указана',
            waiting_time: '~30'
        }
    }
}
</script>

<style scoped>
p{
    margin: 0;
}

.late_screen{
    width: 100%;
    height: 100%;
}

.late_screen>div{
    margin-bottom: 10px;
}
</style>