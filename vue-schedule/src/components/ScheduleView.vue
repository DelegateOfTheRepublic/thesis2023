<template>
    <div class="schedule-container">
        <div class="group_picker" v-if="checkStaffRole()">
            <div>
                <label for="">Направление/специальность: </label>
                <select name="" id="" v-model="specialization">
                    <option selected disabled value>Выберите...</option>
                    <option v-for="spec of specializations" :key="spec.id" :value="spec.id">{{spec.name}}</option>
                </select>
            </div>
            <div>
                <label for="">Курс: </label>
                <select name="" id="" v-model="course">
                    <option selected disabled value>Выберите...</option>
                    <option v-for="course of courses" :key="course.id" :value="course.id">{{course.number}}</option>
                </select>
            </div>
            <div>
                <label for="">Группа: </label>
                <select name="" id="" v-model="study_group">
                    <option selected disabled value>Выберите...</option>
                    <option v-for="group of study_groups" :key="group.id" :value="group.id">{{group.name}}</option>
                </select>
            </div>
            <button @click="getSchedule(study_group)" type="submit">Получить расписание</button>
        </div>
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
            study_days: null,
            specializations: null,
            courses: null,
            study_groups: null,
            specialization: null,
            course: null,
            study_group: null
        }
    },
    async created() {
        if (localStorage.getItem('token') == null) {
            this.$router.push("/login");
        } else {
            if (!this.checkStaffRole()){
                this.getSchedule(JSON.parse(localStorage.getItem('user'))['study_group'])
            } else {
                this.getSpecializations()
                this.getCourses()
                this.getStudyGroups()
            }
        }
    },
    methods: {
        checkStaffRole() {
            return JSON.parse(localStorage.getItem('user'))['role'] !== 'Студент'
        },
        async getSchedule(st_group) {
            console.log(st_group)
            await this.axios.get('http://localhost:8000/api/st_days/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`},
                'params': {
                    'st_group': st_group,
                    'specialization': this.specialization,
                    'course': this.course
                }
            }).then(response => {
                this.study_days = {}

                if (response.data['error']){
                    alert(response.data['error'])
                } else {
                    let tmp = JSON.parse(JSON.stringify(response.data))
                    for (let st_day in tmp){
                        console.log(st_day)
                        if (this.study_days.hasOwnProperty(st_day)){
                            this.study_days[st_day].push(tmp[st_day])
                        } else {
                            this.study_days[st_day] = tmp[st_day]
                        }
                    }
                }
            }).catch(error => {
                console.error(error.response)
            })
        },
        async getSpecializations() {
            this.specializations = {}
            await this.axios.get('http://localhost:8000/api/specializations/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
            }).then(response => {
                this.specializations = JSON.parse(JSON.stringify(response.data))
            }).catch(error => {
                console.error(error.response)
            })
        },
        async getCourses() {
            this.courses = {}
            await this.axios.get('http://localhost:8000/api/courses/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
            }).then(response => {
                this.courses = JSON.parse(JSON.stringify(response.data))
            }).catch(error => {
                console.error(error.response)
            })
        },
        async getStudyGroups() {
            this.study_groups = {}
            await this.axios.get('http://localhost:8000/api/st_groups/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
            }).then(response => {
                this.study_groups = JSON.parse(JSON.stringify(response.data))
            }).catch(error => {
                console.error(error.response)
            })
        }
    }
}

</script>

<style scoped>
.schedule-container{
    width: 90%;
    display: grid;
    gap: 30px;
}

.group_picker{
    width: 65%;
    display: flex;
    justify-content: space-between;
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
    padding: 10px;
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
