<template>
    <div class="teacher_search">
        <select class="teacher_search__deps" name="" id="">
            <option disabled selected hidden>Факультет</option>
        </select>
        <select class="teacher_search__dep_boards" name="" id="">
            <option disabled selected hidden>Кафедра</option>
        </select>
        <div class="search">
            <icon icon_name="icon-search"></icon>
            <input type="text" placeholder="Search...">
        </div>
    </div>
</template>

<script>
import Icon from '../Icon.vue';

export default {
    components: { Icon }
}
</script>

<style scoped>
.teacher_search {
    width: fit-content;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-left: auto;
}

.teacher_search__deps{
    width: 115px;
}

.teacher_search__dep_boards{
    width: 135px;
}

.search {
    display: flex;
    align-items: center;
    gap: 5px;
}

.search>input{
    width: 180px;
}
</style>