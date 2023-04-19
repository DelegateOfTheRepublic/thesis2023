<template>
<div class="group_search">
    <select class="gr_search__courses" name="" id="">
        <option disabled selected hidden>Курс</option>
    </select>
    <select class="gr_search__specs" name="" id="">
        <option disabled selected hidden>Направление</option>
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
.group_search {
    width: fit-content;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.gr_search__courses{
    width: 65px;
}

.gr_search__specs{
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