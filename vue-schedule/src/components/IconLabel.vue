<template>
    <div v-if="showOnlyIcon" class="wrapper" :class="[{'align-center': isTeacher}, {'right-icon': iconPosition == 'right'}]">
        <div name="icon" :class='[icon_name]' class="auto_size" :style="{'font-size': font_size + 'px'}"></div>
        <span><slot></slot></span>
    </div>
    <div v-else name="icon" :class='[icon_name]' class="auto_size" :style="{'font-size': font_size + 'px'}"></div>
</template>

<script>
export default {
    props: {
        icon_name: {
            type: String,
        },
        font_size: {
            type: Number | String,
        },
        iconPosition: {
            type: String,
            default: 'left'
        }
    },
    data(){
        return{
            isTeacher: this.icon_name=='icon-teacher',
            showOnlyIcon: true,
        }
    },
    created() {
        this.setShowSlots()
    },
    beforeUpdate() {
        this.setShowSlots()
    },
    methods: {
        setShowSlots() {
            this.showOnlyIcon = !!this.$slots.default
        }
    }
}
</script>

<style scoped>
.auto_size{
    width: fit-content;
    height: fit-content;
}
.wrapper{
    display: flex;
    gap: 5px;
    white-space: nowrap;

}
.align-center{
    align-items: center;
}
span {
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>