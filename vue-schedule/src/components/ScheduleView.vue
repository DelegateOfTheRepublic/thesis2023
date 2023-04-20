<template>
    <div class="content">
        <aside class="content__left">
            <week-types/>
            <floors/>
        </aside>
        <div class="content__middle">
            <div class="content__middle-head">
                <group-search/>
                <weeks/>
                <teacher-search/>
            </div>
            <div class="content__middle-lessons">
                <lesson-card v-for="i in 6" :key="i"/>
            </div>
        </div>
        <aside class="content__right">
            <exams/>
        </aside>
    </div>
</template>

<script>
import LessonCard from './Schedule View/LessonComponents/LessonCard.vue'
import DayWeek from './DayWeek.vue';
import GroupSearch from './Schedule View/GroupSearch.vue';
import Weeks from './Schedule View/Weeks.vue';
import WeekTypes from './WeekTypes.vue';
import Floors from './Schedule View/Floors.vue';
import Exams from './Schedule View/Exams.vue';
import TeacherSearch from './Schedule View/TeacherSearch.vue';

export default {
    components: {
        LessonCard,
        DayWeek,
        GroupSearch,
        Weeks,
        WeekTypes,
        Floors,
        Exams,
        TeacherSearch
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
        isAdmin() {
            return JSON.parse(localStorage.getItem('user'))['role'] == 'Администратор'
        },
        async getSchedule(st_group) {
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
        },
        setSchedule() {
            localStorage.setItem('schedule', JSON.stringify(this.study_days))
            this.$router.push('/create_schedule')
        }
    }
}

</script>

<style scoped>
.schedule-view {
    display: flex;
    flex: 1;
}
.schedule-view__left {
    flex: 1;
    background-color: aquamarine;
}
.schedule-view__middle {
    width: 1180px;
    background-color: beige;
}
.schedule-view__right {
    flex: 1;
    background-color: aquamarine;
}
.schedule-view__left,
.schedule-view__right {
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: center;
}
.schedule-view__middle-head {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    align-items: center;
}
.schedule-view__middle-lessons {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: 30px;
    margin-top: 40px;
}
.schedule-view__left,
.schedule-view__middle,
.schedule-view__right {
    padding-top: 25px;
}
</style>
