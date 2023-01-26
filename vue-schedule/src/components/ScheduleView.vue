<template>
    <div class="schedule-container">
        <div class="study_day" v-for="(study_day, day) in study_days" :key="day">
            <div class="title">
                <div class="info">
                    <p>{{day}}</p>
                    <p v-if="study_day[0].actual_dates !== null">{{study_day[0].actual_dates}}</p>
                </div>
            </div>
            <div class="study_day-container">
                <div class="study_day-lessons">
                    <lesson-card v-for="lesson of study_day" :key="lesson.id" :lesson_info="lesson"/>
                    <lesson-card v-for="id in (6-study_day.length)" :key="id" :isEmpty="true"/>
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
    },
    data() {
        return {
            study_days: null
        }
    },
    async created() {
        if (localStorage.getItem('token') == null) {
            this.$router.push("/login");
        } else {
            await this.axios.get('http://localhost:8000/api/st_days/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`},
                'st_group': JSON.parse(localStorage.getItem('user'))['study_group']
            }).then(response => {
                this.study_days = {}
                let tmp = JSON.parse(JSON.stringify(response.data))
                for (let st_day of tmp){
                    if (this.study_days.hasOwnProperty(st_day.day_number)){
                        this.study_days[st_day.day_number].push(st_day)
                    } else {
                        this.study_days[st_day.day_number] = [st_day]
                    }
                }
            }).catch(error => {
                console.error(error.response)
            })
        }
    },
}

</script>

<style scoped>
.schedule-container{
    display: grid;
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
