<template>
    <div class="lesson-editor shadow"> <!--11 fields-->
        <transition name="show-notifi">
            <div v-if="showNotifi" class="save">
                Save
            </div>
        </transition>
        <div class="btns">
            <div class="submit" @click="submit()">
                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="25" height="25" x="0" y="0" viewBox="0 0 32 32" style="enable-background:new 0 0 512 512" xml:space="preserve" class="">
                    <title>Подтвердить</title>
                    <g>
                        <g fill="#000">
                            <path d="M12.293 14.707a1 1 0 0 1 0-1.414l3-3a1 1 0 0 1 1.414 0l3 3a1 1 0 0 1-1.414 1.414L17 13.414V18a1 1 0 1 1-2 0v-4.586l-1.293 1.293a1 1 0 0 1-1.414 0zM21 22a1 1 0 1 0 0-2H11a1 1 0 1 0 0 2z" fill="#000000" data-original="#000000" class=""></path>
                            <path fill-rule="evenodd" d="M8.619 3.126A3 3 0 0 1 10.96 2H24a3 3 0 0 1 3 3v22a3 3 0 0 1-3 3H8a3 3 0 0 1-3-3V8.702a3 3 0 0 1 .657-1.875zM10.96 4a1 1 0 0 0-.78.375L7.218 8.077A1 1 0 0 0 7 8.702V27a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1z" clip-rule="evenodd" fill="#000000" data-original="#000000" class=""></path>
                        </g>
                    </g>
                </svg>
            </div>
            <div class="cancel" @click="!showNotifi? $emit('click', $emit) : null">
                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="25" height="25" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve" class="">
                    <title>Отменить создание</title>
                    <g>
                        <g data-name="Layer 2">
                            <path d="M18 22.75H6A4.756 4.756 0 0 1 1.25 18V6A4.756 4.756 0 0 1 6 1.25h12A4.756 4.756 0 0 1 22.75 6v12A4.756 4.756 0 0 1 18 22.75zm-12-20A3.254 3.254 0 0 0 2.75 6v12A3.254 3.254 0 0 0 6 21.25h12A3.254 3.254 0 0 0 21.25 18V6A3.254 3.254 0 0 0 18 2.75z" fill="#000000" data-original="#000000" class=""></path>
                            <path d="M15.535 16.286a.748.748 0 0 1-.53-.22L7.934 8.995a.75.75 0 1 1 1.061-1.061l7.07 7.071a.751.751 0 0 1-.53 1.281z" fill="#000000" data-original="#000000" class=""></path>
                            <path d="M8.464 16.286a.751.751 0 0 1-.53-1.281l7.071-7.071a.75.75 0 0 1 1.06 1.061l-7.07 7.071a.752.752 0 0 1-.531.22z" fill="#000000" data-original="#000000" class=""></path>
                        </g>
                    </g>
                </svg>
            </div>
        </div>
        <div class="lesson_time_range">
            <div class="title">
                <p>Время пары</p>
            </div>
            <div class="time_range_picker">
                <div>
                    <label for="">С</label>
                    <input type="time" name="start_time" id="" v-model="startTime">
                </div>
                <div>
                    <label for="">До</label>
                    <input type="time" name="end_time" id="" v-model="endTime">
                </div>
            </div>
        </div>
        <div class="subject">
            <label for="">Дисциплина</label>
            <select name="subject" id="" v-model="subject">
                <option selected disabled value>Выберите...</option>
                <option v-for="subject of subjects"
                        :key="subject.id"
                        :value="subject.id">
                    {{subject.name}}
                </option>
            </select>
        </div>
        <div class="teacher">
            <label for="">Преподаватель</label>
            <select name="teacher" id="" v-model="teacher">
                <option selected disabled value>Выберите...</option>
                <option v-for="teacher of teachers"
                        :key="teacher.id"
                        :value="teacher.id">
                    {{teacher.first_name + ` ${teacher.last_name[0]}.` + `${teacher.middle_name[0]}.`}}
                </option>
            </select>
        </div>
        <div class="room">
            <label for="">Аудитория</label>
            <select name="room" id="" v-model="room">
                <option selected disabled value>Выберите...</option>
                <option v-for="room of rooms"
                        :key="room.id"
                        :value="room.id">
                    {{room.number}}
                </option>
            </select>
        </div>
        <div class="study-format">
            <label for="">Дист. формат?</label>
            <input type="checkbox" name="study_format" id="">
        </div>
        <div class="is-fractional">
            <label for="">Дробная пара?</label>
            <input type="checkbox" name="is_fractional" id="" v-model="isFractional">
        </div>
        <div class="is-top-week">
            <label for="">Относится к верхней недели?</label>
            <input type="checkbox" name="is_top_week" id="" v-model="isTopWeek">
        </div>
        <div class="start-date">
            <label for="">С какого числа</label>
            <input type="date" name="start_date" v-model="startDate" min="2023-01-01" max="2023-12-31">
        </div>
        <div class="end-date">
            <label for="">По какое число</label>
            <input type="date" name="end_date" v-model="endDate" :min="startDate" max="2023-12-31">
        </div>
    </div>
</template>

<script>
export default {
emits: [''],
props: ['submitCreateStDay'],
data() {
    return {
            isTopWeek: false,
            isFractional: false,
            startDate: new Date().toJSON().slice(0, 10),
            endDate: '',
            startTime: '08:30:00',
            endTime: '09:50:00',
            subject: '',
            teacher: '',
            room: '',
            isRemoteFormat: false,
            subjects: null,
            teachers: null,
            rooms: null,
            showNotifi: false
        }
    },
    created() {
        this.checkSchedule()
        this.getSubjects()
        this.getTeachers()
        this.getRooms()
    },
watch: {
        isTopWeek: function () {
            if (!this.isFractional && this.isTopWeek){
                this.isFractional = true
            }
        },
        isFractional: function () {
            if (!this.isFractional){
                this.isTopWeek = false
            }
        },
        endDate: function () {
            if (new Date(this.endDate) < new Date(this.startDate)){
                this.endDate = this.startDate
            }
        }
    },
    methods: {
        checkSchedule() {
            console.log(localStorage.getItem('schedule'))
            if (localStorage.getItem('schedule') !== null){
                console.log('asd')
            }
        },
        async getSubjects() {
            this.subjects = {}
            await this.axios.get('http://localhost:8000/api/subjects/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
            }).then(response => {
                this.subjects = JSON.parse(JSON.stringify(response.data))
            }).catch(error => {
                console.error(error.response)
            })
        },
        async getTeachers() {
            this.teachers = {}
            await this.axios.get('http://localhost:8000/api/teachers/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
            }).then(response => {
                this.teachers = JSON.parse(JSON.stringify(response.data))
            }).catch(error => {
                console.error(error.response)
            })
        },
        async getRooms() {
            this.rooms = {}
            await this.axios.get('http://localhost:8000/api/rooms/', {
                'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
            }).then(response => {
                this.rooms = JSON.parse(JSON.stringify(response.data))
            }).catch(error => {
                console.error(error.response)
            })
        },
        submit() {
            this.submitCreateStDay({
                is_top_week: this.isTopWeek,
                is_fractional: this.isFractional,
                start_date: this.startDate,
                end_date: this.endDate,
                start_time: this.startTime,
                end_time: this.endTime,
                subject: this.subject,
                teacher: this.teacher,
                room: this.room,
                study_format: (this.isRemoteFormat) ? 1 : null,

            })
            this.showNotifi = true
        }
    }
}
</script>

<style scoped>
.save{
    display: block;
    position: absolute;
    transform: translateY(-200px);
    left: 44%;
    background-color: rgba(0, 255, 68, 0.479);
    border-radius: 5px;
    padding: 5px;
    transition: all 0.5s ease-in;
}

.save_show{
    display: block;
    top: 0px;
    transition: all 0.5s ease-in;
    transition-delay: 5s;
}

.save-notifi-enter-active {
    transform: translateY(-180px);
  transition: all 0.3s ease-out;
}

.save-notifi-leave-active {
    transform: translateY(-180px);
  transition: all 0.8s ease-in
}

.save-notifi-enter-from,
.save-notifi-leave-to {
  transform: translateY(-180px);
}

.lesson-editor{
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 5px;
    padding-left: 15px;
    padding-right: 15px;
}

.shadow{
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}

.btns{
    position: absolute;
    bottom: 10px;
    right: 10px;
    display: flex;
    flex-direction: column;
}

.cancel:hover{
    cursor: pointer;
}

.submit:hover{
    cursor: pointer;
}

.lesson_time_range{
    height: 22%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: 1px solid rgb(194, 193, 193);
    border-radius: 10px;
}

.title{
    border-bottom: 1px solid rgb(194, 193, 193);
    padding: 5px;
}

.time_range_picker{
    display: flex;
    justify-content: space-between;
    padding: 5px;
}

p{
    margin: 0;
}
</style>