<template>
    <div class="pagination">
        <v-button :iconName="'icon-arrow_left'" :fontSize="10"/>
        <span>1 из 10</span>
        <v-button :iconName="'icon-arrow_right'" :fontSize="10"/>
    </div>
</template>

<script>
import VButton from './VButton.vue';

export default {
    components: {
        VButton
    },
    data() {
        return {

        }
    }
}
</script>

<style scoped>
.pagination {
    width: fit-content;
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 10px auto 0;

    background-color: cornflowerblue;
}
</style>