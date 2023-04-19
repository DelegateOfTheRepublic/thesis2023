<template>
    <!-- <auditories/> -->
    <!-- <department-boards/> -->
    <!-- <subjects/> -->
    <!-- <study-groups/> -->
    <uni-staff/>
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