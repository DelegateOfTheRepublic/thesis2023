<template>
<div class="homework">
    <icon icon_name="icon-arrow_back" font_size='15'></icon>
    <div class="homework__warning">
        <p>До здачи д/з осталось: 1 день</p>
        <icon icon_name="icon-warning" font_size="15"></icon>
    </div>
    <p>Описание домашнего заданияфывыфафыафывпаывпакпурврфрфеурафпфып</p>
</div>
</template>

<script>
export default {

}
</script>

<style scoped>
.homework{
    width: 100%;
    height: 100%;
}

.homework>div[name="icon"] {
    margin-bottom: 10px;
}

.homework__warning{
    display: flex;
    align-items: center;
}

.homework>p{
    word-break: break-all;
}

p{
    margin: 0;
}
</style>