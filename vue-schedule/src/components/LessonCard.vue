<template>
    <div>
        <div class="info">
            <p>Пара 1</p>
            <p>8:30 - 9:50</p>
        </div>
        <div class="lesson-card">
            <div class="lesson-card__title">
                <p class="lesson-card__info">Математическое программирование</p>
            </div>
            <div class="wrapper">
                <div class="lesson-card__content">
                    <div class="lesson-card__aud_format">
                        <p>Ауд. 511</p>
                        <p>(с 08.09)</p>
                        <p>ДФ</p>
                    </div>
                    <p class="lesson-card__teacher">доц. Полупанов Д. В.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
.wrapper{
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex-grow: 1;
}

.lesson-card{
    display: flex;
    flex-direction: column;
    width: 250px;
    height: 180px;
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}

.lesson-card__title{
    padding: 10px;
    border-bottom: 1px dashed gray;
}

.separator{
    width: 3px;
    background-color: gray;
    border-radius: 5px;
    margin-right: 10px;
}

.lesson-day{
    flex-grow: 1;
}

.lesson-card__teacher{
    width: fit-content;
}

.lesson-card__content{
    display: flex;
    height: 50%;
    justify-content: space-between;
    flex-direction: column;
    align-content: center;
    align-items: center;
}

.lesson-card__info{
    overflow-wrap: break-word;
    text-align: center;
}

.lesson-card__aud_format{
    width: 80%;
    display: flex;
    justify-content: space-between;
}

.info{
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
}

.info>p{
    border: 2px solid gainsboro;
    border-radius: 7px;
    padding: 1px;
    padding-left: 5px;
    padding-right: 5px;
}

p{
    margin: 0px;
    pointer-events: none;
}
</style>
