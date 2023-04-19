<template>
<div class="online_lesson">
    <icon icon_name="icon-arrow_back" font_size='15'></icon>
    <p>Платформа: {{meeting.platform}}</p>
    <p>Идентификатор: {{meeting.id}}</p>
    <p>Код доступа: {{meeting.passcode}}</p>
    <div class="wrapper">
        <div class="online_lesson__buttons">
            <input type="button" value="Подключиться"/>
            <input type="button" value="Получить ссылку"/>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{
            meeting: {
                'platform': 'Zoom',
                'id': '781 1759 9561',
                'passcode': 'i6ReG3'
            }
        }
    }
}
</script>

<style scoped>
.online_lesson {
    position: relative;
    width: 100%;
    height: 100%;
}

.online_lesson>div[name="icon"]{
    margin-bottom: 10px;
}

.wrapper{
    position: absolute;
    width: 100%;
    bottom: 0;
}

.online_lesson__buttons {
    width: fit-content;
    display: flex;
    gap: 20px;
    margin: auto;
}

.online_lesson__buttons>input{
    font-size: 12px;
}

p{
    margin: 0;
}
</style>