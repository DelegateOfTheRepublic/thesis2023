<template>
    <div class="schedule-container">
        <div class="study_day">
            <div class="title">
                <div class="info">
                    <p>Понедельник</p>
                    <p>12.12.2023 - 12.12.2023</p>
                </div>
            </div>
            <div class="study_day-container">
                <div class="study_day-lessons">
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                </div>
            </div>
        </div>

        <div class="study_day">
            <div class="title">
                <div class="info">
                    <p>Понедельник</p>
                    <p>12.12.2023 - 12.12.2023</p>
                </div>
            </div>
            <div class="study_day-container">
                <div class="study_day-lessons">
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                    <lesson-card/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import LessonCard from './LessonCard.vue'
export default {
  components: {
    LessonCard
  }
}

</script>

<style scoped>
.schedule-container{
    display: grid;
    grid-template-rows: repeat(2, 1fr);
    gap: 30px;
}

.study_day-container{
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
    padding: 15px;
}

.study_day-lessons{
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 30px;
}

.title{
    margin-bottom: 20px;
}

.info{
    display: flex;
    justify-content: space-between;
    width: 23%;
}

.info>p{
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}

p{
    margin: 0px;
    padding: 5px;
    padding-left: 8px;
    padding-right: 8px;
}
</style>
