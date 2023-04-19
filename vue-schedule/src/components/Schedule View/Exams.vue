<template>
<div class="exams">
    <p>{{title}}</p>
    <div class="exams__list">
        <div class="exam" v-for="i in 5" :key="i">
            <div class="exam__title">
                <p>{{subject}}</p>
                <p>{{teacher.position}} {{teacher.name}}</p>
            </div>
            <div class="exam__info">
                <div>
                    <p>Консультация</p>
                    <div>
                        <p>{{consult.date}}</p>
                        <p>ауд. {{consult.audit}}</p>
                    </div>
                </div>
                <div>
                    <p>Экзамен</p>
                    <div>
                        <p>{{exam.date}}</p>
                        <p>ауд. {{exam.audit}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <slider/>
</div>
</template>

<script>
import Slider from '../Slider.vue'
export default {
  components: { Slider },
  data(){
      return{
          title: 'Расписание экзаменов',
          subject: 'Проектирование ИС',
          teacher: {'position': 'доц.',
                    'name': 'Путинцева А.А.'},
          consult: {
              'date': '01.06',
              'audit': '503'
          },
          exam: {
              'date': '03.06',
              'audit': '524'
          }
      }
  }
}
</script>

<style scoped>
p{
    margin: 0;
}

.exams {
    width: fit-content;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    padding: 10px;
    background-color: cadetblue;
}

.exams__list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.exam {
    padding: 5px;
    background-color: bisque;
}

.exam__title {
    text-align: center;
}

.exam__info {
    display: flex;
    gap: 30px;
    padding-top: 10px;
}

.exam__info{
    text-align: center;
}

.exam__info>div>div {
    display: flex;
    gap: 8px;
}
</style>