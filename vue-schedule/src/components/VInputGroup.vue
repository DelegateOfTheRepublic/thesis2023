<template>
    <div class="v-input-group">
        <div v-if="title" class="v-input-group__title">
            <span>{{ title }}</span>
        </div>
        <div :class="['v-input-group__inputs', directionClass()]">
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            title: {
                type: String
            },
            direction: {
                type: String,
                default: 'col'
            }
        },
        methods: {
            directionClass() {
                return this.direction !== 'col'? 'v-input-group__inputs--row' : 'v-input-group__inputs--col'
            },

        },
        created() {
            console.log(this.$slots.default[0].componentOptions.propsData)
        }
    }
</script>

<style scoped>
.v-input-group {

}
.v-input-group__title {
    display: flex;
    justify-content: space-between;
}
.v-input-group__inputs,
.v-input-group__inputs--col,
.v-input-group__inputs--row {
    display: flex;
    gap: 6px;
}
.v-input-group__inputs--col {
    flex-direction: column;
}
.v-input-group__inputs--row {
    flex-direction: row;
    gap: 0;
    justify-content: space-between;
}
</style>