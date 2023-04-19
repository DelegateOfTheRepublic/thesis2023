<template>
    <div class="search-bar">
            <div v-if="departmentSelect" class="search-bar__select">
                <span>Факультет:</span>
                <select name="" id="">
                    <option value="">ФМиИТ</option>
                </select>
            </div>
            <div v-if="search" class="search-bar__input">
                <icon icon_name="icon-search" font_size="16"/>
                <input type="text" placeholder="Search..."/>
            </div>
        </div>
</template>

<script lang="js">
import Icon from './Icon.vue';

export default {
    props: {
        search: {
            type: Boolean,
            default: true
        },
        departmentSelect: {
            type: Boolean,
            default: true
        }
    },
    components: { Icon }
}
</script>

<style scoped>
.search-bar {
    margin-top: 10px;

    background-color: cornflowerblue;
}
.search-bar__select {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.search-bar__input {
    display: flex;
    align-items: center;
    gap: 6px;
}
.search-bar__input>input {
    width: 100%;
}
</style>