<template>
    <div class="content">
        <div class="content__left"></div>
        <div class="content__middle content--flex content--flex-sb">
            <div class="content--flex content--flex-col">
                <auditories/>
                <uni-staff style="margin-top: 25px;"/>
            </div>
            <div class="content--flex content--flex-col">
                <study-groups/>
                <department-boards style="margin-top: 25px;"/>
            </div>
            <div class="content--flex content--flex-col">
                <subjects/>
            </div>
        </div>
        <div class="content__right"></div>
    </div>
</template>

<script>
import Auditories from './Components/Auditories.vue'
import DepartmentBoards from './Components/DepartmentBoards.vue'
import StudyGroups from './Components/StudyGroups.vue'
import Subjects from './Components/Subjects.vue'
import UniStaff from './Components/UniStaff.vue'
export default {
    components: { Auditories, DepartmentBoards, Subjects, StudyGroups, UniStaff }
}
</script>

<style scoped>

</style>