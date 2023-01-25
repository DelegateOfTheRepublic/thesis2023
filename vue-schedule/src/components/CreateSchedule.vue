<template>
    <div class="schedule-wrapper">
        <div class="schedule-explorer shadow">
            <div>
                <label for="">День недели:</label>
                <select name="" id=""></select>
            </div>
            <div class="specialization">
                <label for="">Напр.-е/спец.-ть:</label>
                <select name="" id=""></select>
            </div>
            <div>
                <label for="">Курс:</label>
                <select name="" id=""></select>
            </div>
            <div>
                <label for="">Группа:</label>
                <select name="" id=""></select>
            </div>
        </div>
        <div class="schedule-workspace shadow">
            <div class="schedule-menu">
                <div class="study-day">
                    <p>Понедельник</p>
                </div>
                <div class="study-group-info">
                    <div>
                        <p>Группа: 41</p>
                    </div>
                    <div>
                        <p>Напр.-е/спец.-ть: ПИ</p>
                    </div>
                    <div>
                        <p>Курс: 4</p>
                    </div>
                </div>
                <div class="save-btn">
                    <p>Сохранить</p>
                </div>
            </div>
            <div class="workspace-wrapper">
                <lesson-placeholder/>
                <lesson-placeholder/>
                <lesson-placeholder/>
                <lesson-placeholder/>
                <lesson-placeholder/>
                <lesson-placeholder/>
            </div>
        </div>
        <div class="schedule-templates shadow">

        </div>
    </div>
</template>

<script>
import LessonPlaceholder from './LessonPlaceholder.vue'

export default {
  components: {
        LessonPlaceholder,
  }
}

</script>

<style scoped>
.container{
    margin-top: 40px;
}

.schedule-wrapper{
    display: flex;
    justify-content: space-between;
    width: 90%;
    height: 850px;
    margin-top: -40px;
}

.shadow{
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}

.schedule-explorer{
    width: 15%;
    height: 25%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 10px;
}

.schedule-workspace{
    width: 65%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-content: center;
    align-items: center;
}

.workspace-wrapper{
    display: grid;
    width: 96%;
    height: 90%;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 15px;
}

.schedule-templates{
    width: 15%;
}

.schedule-menu{
    width: 96%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.study-group-info{
    width: 50%;
    display: flex;
    justify-content: space-between;
}

.study-day, .study-group-info>div, .save-btn{
    border: 2px solid gainsboro;
    border-radius: 7px;
    padding: 5px;
    padding-left: 10px;
    padding-right: 10px;
    transition: all 0.2s ease-in-out;
}

.save-btn:hover{
    cursor: pointer;
    background-color: gainsboro;
}

.specialization{
    height: 25%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

p{
    pointer-events: none;
    margin: 0;
}
</style>
