<template>
<div class="tab-list">
    <div class="tab-list__item" v-for="i in 3" :key="i">
        <span>{{ studyGroup }}</span>
        <div class="tab-list__item-actions menu">
            <icon icon_name="icon-close" font_size="15"/>
            <div class="menu__item--standart">
                <icon icon_name="icon-more" font_size="15"/>
                <div class="drop-menu">
                    <v-button :iconName="'icon-add'" :fontSize="'15'" :title="'Расписание экзаменов'"/>
                    <v-button :iconName="'icon-open'" :fontSize="'15'" :title="'Расписание пересдач'"/>
                </div>
            </div>
        </div>
    </div>
    <div class="tab-list__item-add menu__item--standart">
        <icon icon_name="icon-add" font_size="12"/>
        <new-schedule class="drop-menu"/>
    </div>
</div>
</template>

<script>
import Icon from '../Icon.vue'
import IconLabel from '../IconLabel.vue'
import VButton from '../VButton.vue'
import NewSchedule from './NewSchedule.vue'

export default {
  components: { Icon, IconLabel, VButton, NewSchedule },
    data() {
        return{
            studyGroup: 'ПИ-4ИВТ186А'
        }
    }
}
</script>

<style scoped>
.tab-list {
    display: flex;
    align-items: center;
    gap: 20px;
    background-color: bisque;
}
.tab-list__item {
    display: flex;
    gap: 10px;
    background-color: cadetblue;
}
.tab-list__item-actions {
    display: flex;
    align-items: center;
    gap: 2px;
}
.tab-list__item-add {
    margin-left: auto;
}
</style>