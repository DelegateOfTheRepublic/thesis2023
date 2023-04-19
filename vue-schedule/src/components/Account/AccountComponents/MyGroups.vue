<template>
    <div class="my-groups">
        <span>Мои группы</span>
        <div class="my-groups__list">
            <div class="my-group__list-item" v-for="i in 2" :key="i">
                <span>{{ groupCourse }}-й курс</span>
                <div class="my-group__item-wrapper">
                    <icon-label :icon_name="'icon-group_list'" :font_size="20">{{ studyGroup.variantA }}</icon-label>
                    <icon-label :icon_name="'icon-group_list'" :font_size="20">{{ studyGroup.variantB }}</icon-label>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import IconLabel from '../../IconLabel.vue'

export default {
    components: {
        IconLabel
    },
    data() {
        return {
            groupCourse: '4',
            studyGroup: {
                'variantA': 'ПИ-4ИВТ186А',
                'variantB': 'МОАИС-4ИВТ177П'
            }
        }
    }
}
</script>

<style scoped>
.my-groups {
    background-color: bisque;
}
.my-groups__list {
    display: flex;
    gap: 30px;
    margin-top: 15px;
}
.my-group__list-item {
    background-color: cornflowerblue;
}
.my-group__item-wrapper {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}
</style>