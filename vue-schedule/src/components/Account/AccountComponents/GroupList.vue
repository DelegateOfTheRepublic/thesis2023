<template>
    <div class="group-list">
        <div class="group-list__head">
            <span>Список группы {{ studyGroup }}</span>
            <div class="head__btns">
                <v-button :iconName="'icon-download'" :fontSize="18"/>
                <v-button :iconName="'icon-close'" :fontSize="18"/>
            </div>
        </div>
        <div class="group-list__students">
            <span v-for="student in studyGroupList" :key="student.name">{{ student.name }}</span>
        </div>
    </div>
</template>

<script>
import VButton from '../../VButton.vue'

export default {
    components: {
        VButton
    },
    data() {
        return {
            studyGroup: 'ПИ-4ИВТ186А',
            studyGroupList: [
                {'name': 'Студент А.А.'},
                {'name': 'Студент Б.Б.'},
                {'name': 'Студент В.В.'}
            ]
        }
    }
}
</script>

<style scoped>
.group-list {
    background-color: bisque;
}
.group-list__head {
    display: flex;
    gap: 25px;
    align-items: center;
}
.head__btns {
    display: flex;
    gap: 8px;
}
.group-list__students {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 15px;
}
</style>