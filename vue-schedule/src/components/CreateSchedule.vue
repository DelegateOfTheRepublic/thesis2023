<template>
    <!-- <view-lesson-card/> -->
    <!-- <edit-lesson-card/> -->
    <!-- <tool-bar/> -->
    <!-- <templates-explorer/> -->
    <!-- <child-items/> -->
    <!-- <tabs/> -->
    <!-- <new-schedule/> -->
    <!-- <to-duplicate/> -->
    <!-- <overlap-info/> -->
    <!-- <small-template/> -->
    <!-- <lesson-split/> -->
    <!-- <add-group/> -->
    <add-conference/>
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
  },
  data() {
    return {
            courses: null,
            study_groups: null,
            specializations: null,
            day: '',
            specialization: '',
            course: '',
            study_group: '',
            res: {}
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
    width: 55%;
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
