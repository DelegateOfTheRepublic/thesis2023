<template>
<div :class="[title? 'button' : 'icon-button', iconPosition==='right'? 'right-icon' : null]" id="v-button">
    <icon :icon_name='iconName' :font_size='fontSize'></icon>
    <p v-if="title">{{title}}</p>
</div>
</template>

<script>
import Icon from './Icon.vue';

export default {
    name: 'v-button',
    props:{
        title:{
            type: String,
            validator: function(value) {
                return value.length !== 0
            }
        },
        iconName: {
            type: String
        },
        fontSize: {
            type: [String, Number]
        },
        iconPosition: {
            type: String,
            default: 'left'
        }
    },
    components: {
        Icon
    }
}
</script>

<style scoped>
.button {
    display: inline-flex;
    width: fit-content;
    height: fit-content;
    align-items: center;
    gap: 5px;
    background-color: coral;
}

.icon-button {
    width: fit-content;
    height: fit-content;
    background-color: coral;
}

.right-icon {
    flex-direction: row-reverse;
}

p {
    margin: 0;
    white-space: nowrap;
}
</style>