<template>
    <div class="uni-staff">
        <div class="uni-staff__head">
            <span>Состав ВУЗ'а</span>
            <div class="uni-staff__head-btns">
                <v-button :iconName="'icon-add'" :fontSize="15" @click.native="showAddStaffForm"/>
                <v-button :iconName="'icon-params'" :fontSize="19" @click.native="showUniStaffFilter"/>
            </div>
        </div>
        <div class="uni-staff__staff-type">
            <v-button :iconName="'icon-radio_checked'" :fontSize="15" :title="'Студенты'"/>
            <v-button :iconName="'icon-radio_unchecked'" :fontSize="15" :title="'Преподаватели'"/>
        </div>
        <div class="uni-staff__add-staff" v-if="showAddStaff">
            <v-input-group title="ФИО">
                <v-input :placeholder="'Имя'"/>
                <v-input :placeholder="'Фамилия'"/>
                <v-input :placeholder="'Отчество'"/>
            </v-input-group>
            <v-input-group title="Контакты">
                <v-input :placeholder="'myemail@mail.ru'"/>
                <v-input :placeholder="'+7 (911) 456-78-90'"/>
            </v-input-group>
            <v-input-group title="Рабочая информация" direction="row" v-if="isTeacher">
                <select name="" id="">
                    <option disabled selected value="">Должность</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Факультет</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Кафедра</option>
                </select>
            </v-input-group>
            <v-input-group title="Учебная информация" v-if="isStudent">
                <select name="" id="">
                    <option disabled selected>Группа</option>
                    <option value="">ПИ-4ИВТ186А</option>
                </select>
            </v-input-group>
            <div class="add-staff__submition">
                <v-button :iconName="'icon-submit'" :fontSize="15" :title="'Добавить'"/>
                <v-button :iconName="'icon-cancel'" :fontSize="15" :title="'Отмена'"/>
            </div>
        </div>
        <div class="uni-staff__filter" v-if="showStaffFilter">
            <v-input-group v-if="isStudent">
                <select name="" id="">
                    <option disabled selected value="">Высшее образование</option>
                    <option value="">Бакалавриат</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Факультет</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Направление подготовки</option>
                    <option value="">ПИ</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Курс</option>
                    <option value="">4</option>
                </select>
            </v-input-group>
            <v-input-group direction="row" v-if="isTeacher">
                <select name="" id="">
                    <option disabled selected value="">Факультет</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Кафедра</option>
                </select>
                <select name="" id="">
                    <option disabled selected value="">Должность</option>
                </select>
            </v-input-group>
        </div>
        <div class="uni-staff__list">
            <icon-label :icon_name="'icon-avatar'" :font_size="22" v-for="i in 10" :key="i">Антон В.Б.</icon-label>
        </div>
    </div>
</template>

<script>
import Icon from '../../Icon.vue';
import VButton from '../../VButton.vue'
import VInput from '../../VInput.vue';
import IconLabel from '../../IconLabel.vue';
import VInputGroup from '../../VInputGroup.vue';

export default {
  components: { VButton, VInput, IconLabel, VInputGroup },
  data() {
    return {
        isStudent: true,
        isTeacher: false,
        showAddStaff: false,
        showStaffFilter: false
    }
  },
  methods: {
    showAddStaffForm(event) {
        this.showAddStaff = !this.showAddStaff
    },
    showUniStaffFilter(event) {
        this.showStaffFilter = !this.showStaffFilter
    }
  }
}
</script>

<style scoped>
.uni-staff {
    width: 350px;
}
.uni-staff__head {
    display: flex;
    justify-content: space-between;

    background-color: cornflowerblue;
}
.uni-staff__head-btns {
    display: flex;
    gap: 12px;
    align-items: center;
}
.uni-staff__staff-type {
    display: flex;
    gap: 30px;
    justify-content: center;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.uni-staff__add-staff {
    margin-top: 10px;

    background-color: cornflowerblue;
}
.add-staff__submition {
    display: flex;
    gap: 50px;
    justify-content: center;
    margin-top: 12px;
}
.uni-staff__filter {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 10px;

    background-color: cornflowerblue;
}
.uni-staff__list {
    margin-top: 10px;

    background-color: cornflowerblue;
}
</style>