<template>
    <div class="content">
        <div class="content__left">
            <div class="study-group-info">
                <p>Группа: {{ studyGroup.name }}</p>
                <p>Курс: {{ studyGroup.course }}</p>
                <p>Направление: {{ studyGroup.specialization }}</p>
                <p>Факультет: {{ studyGroup.department }}</p>
                <p>Форма обучения: {{ studyGroup.studyFormat }}</p>
                <div class="study-group-info__semester">
                    <p>Семестр: {{ semester.number }}</p>
                    <div>
                        <span>С: {{ semester.startDate }}</span>
                        <span>По: {{ semester.endDate }}</span>
                    </div>
                </div>
            </div>
            <week-types/>
        </div>
        <div class="content__middle">
            <div class="schedule-creator">
                <tabs/>
                <div class="schedule-creator__workspace">
                    <weeks size="medium" class="center"/>
                    <div class="schedule-creator__lessons">
                        <div class="schedule-creator__lessons-row1">
                            <view-lesson-card v-for="i in 2" :key="i"/>
                            <edit-lesson-card/>
                        </div>

                        <div class="schedule-creator__lessons-row2">
                            <view-lesson-card v-for="i in 2" :key="i"/>
                            <edit-lesson-card/>
                        </div>
                    </div>
                </div>
                <to-duplicate/>
            </div>
        </div>
        <div class="content__right">
            <templates-explorer/>
            <overlap-info/>
        </div>
    </div>
</template>

<script>
import AddConference from './CreateSchedule/AddConference.vue'
import AddGroup from './CreateSchedule/AddGroup.vue'
import ChildItems from './CreateSchedule/ChildItems.vue'
import EditLessonCard from './CreateSchedule/EditLessonCard.vue'
import LessonSplit from './CreateSchedule/LessonSplit.vue'
import NewSchedule from './CreateSchedule/NewSchedule.vue'
import OverlapInfo from './CreateSchedule/OverlapInfo.vue'
import SmallTemplate from './CreateSchedule/SmallTemplate.vue'
import Tabs from './CreateSchedule/Tabs.vue'
import TemplatesExplorer from './CreateSchedule/TemplatesExplorer.vue'
import ToDuplicate from './CreateSchedule/ToDuplicate.vue'
import ToolBar from './CreateSchedule/ToolBar.vue'
import ViewLessonCard from './CreateSchedule/ViewLessonCard.vue'
import LessonPlaceholder from './LessonPlaceholder.vue'
import Weeks from './Schedule View/Weeks.vue'
import WeekTypes from './WeekTypes.vue'

export default {
  components: {
        LessonPlaceholder,
        ViewLessonCard,
        EditLessonCard,
        ToolBar,
        TemplatesExplorer,
        ChildItems,
        Tabs,
        NewSchedule,
        ToDuplicate,
        OverlapInfo,
        SmallTemplate,
        LessonSplit,
        AddGroup,
        AddConference,
        WeekTypes,
    Weeks
  },
  data() {
    return {
            studyGroup: {
                name: 'ПИ-4ИВТ186А',
                course: '4',
                specialization: 'Прикладная информатика',
                department: 'ФМиИТ',
                studyFormat: 'очный'
            },
            semester: {
                number: '1',
                startDate: '01.09.22',
                endDate: '31.12.22'
            }
      }
  },
  created() {
      this.getSpecializations()
      this.getCourses()
      this.getStudyGroups()
  },
  methods: {
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
        submitCreateStDay(data){
            let res = data
            res['day_number'] = this.day
            res['study_group'] = this.study_group
            if (this.res.hasOwnProperty(this.day)){
                this.res[this.day].push(res)
            } else {
                this.res[this.day] = [res]
            }
        },
        async saveSchedule() {
            await this.axios.post('http://localhost:8000/api/st_days/',
            this.res,
            {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`},
            }).then(response => {

            }).catch(error => {
                console.error(error.response)
            })
        }
    }
}

</script>

<style scoped>
.study-group-info {
    background-color:cornflowerblue;
}
.study-group-info,
.study-group-info__semester {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.study-group-info__semester {
    background-color: blueviolet;
    gap: 15px;
}
.study-group-info__semester>div {
    display: flex;
    gap: 30px;
}
.schedule-creator {

}
.schedule-creator__workspace {
    margin-top: 30px;
}
.schedule-creator__lessons {
    margin-top: 20px;
}
.schedule-creator__lessons-row1,
.schedule-creator__lessons-row2 {
    display: flex;
    justify-content: space-between;
}
.schedule-creator__lessons-row1 {
}
.schedule-creator__lessons-row2 {
    margin-top: 25px;
}
</style>
