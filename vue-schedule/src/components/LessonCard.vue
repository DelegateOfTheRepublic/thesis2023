<template>
    <div>
        <div class="info">
            <p>Пара {{lesson_info.lesson.ordinal_number}}</p>
            <p>{{getNormTime(lesson_info.lesson.start_time)}} - {{getNormTime(lesson_info.lesson.end_time)}}</p>
        </div>
        <div class="lesson-card">
            <div class="lesson-card__title">
                <p class="lesson-card__info">{{lesson_info.subject}}</p>
            </div>
            <div class="wrapper">
                <div class="lesson-card__content">
                    <div class="lesson-card__aud_format">
                        <p>{{lesson_info.room}}</p>
                        <p>(с {{getNormDate(lesson_info.start_date)}})</p>
                        <p>{{lesson_info.study_format}}</p>
                    </div>
                    <p class="lesson-card__teacher">{{lesson_info.position}} {{lesson_info.teacher}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['lesson_info', 'isEmpty'],
    methods: {
        getNormDate(date) {
            let newDate = date.split('-')
            return `${newDate[2]}.${newDate[1]}`
        },
        getNormTime(time) {
            let newTime = time.split(':')
            return `${newTime[0]}:${newTime[1]}`
        }
    }
}
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

.empty>p{
    background-color: rgba(146, 146, 146, 0.762);
}

.lesson-card--empty{
    background-color: rgba(146, 146, 146, 0.762);
}

p{
    margin: 0px;
    pointer-events: none;
}
</style>
