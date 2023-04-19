<template>
    <div v-if="showOnlyIcon" class="wrapper" :class="{'align-center': isTeacher}">
        <div name="icon" :class='[icon_name]' class="auto_size" :style="{'font-size': font_size + 'px'}"></div>
        <slot></slot>
    </div>
    <div v-else name="icon" :class='[icon_name]' class="auto_size" :style="{'font-size': font_size + 'px'}"></div>
</template>

<script>
export default {
    props: ['icon_name', 'font_size'],
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
}

.align-center{
    align-items: center;
}
p {
    margin: 0;
}
</style>