<template>
    <div class="lesson-editor shadow"> <!--11 fields-->
        <div class="cancel" @click="$emit('click', $emit)">
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
            <select name="subject" id=""></select>
        </div>
        <div class="teacher">
            <label for="">Преподаватель</label>
            <select name="teacher" id=""></select>
        </div>
        <div class="room">
            <label for="">Аудитория</label>
            <select name="room" id=""></select>
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
emits: [],
data() {
    return {
            isTopWeek: false,
            isFractional: false,
            startDate: new Date().toJSON().slice(0, 10),
            endDate: '',
            startTime: '08:30:00',
            endTime: '09:50'
        }
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
        endDate: function() {
            if (new Date(this.endDate) < new Date(this.startDate)){
                this.endDate = this.startDate
            }
        }
    }
}
</script>

<style scoped>
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

.cancel{
    position: absolute;
    bottom: 10px;
    right: 10px;
}

.cancel:hover{
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