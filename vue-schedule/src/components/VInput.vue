<template>
    <div class="v-input" v-if="!showError">
        <span v-if="label">{{ label }}</span>
        <input :type="type" :placeholder="placeholder"/>
    </div>
    <div v-else class="v-input__type-error">
        <span>Неверный тип input'а</span>
    </div>
</template>

<script>
import Icon from './Icon.vue';

const AvailableTypes = {
    Text: 'text',
    Password: 'password',
    Email: 'email',
    Tel: 'tel'
}

export default {
    name: 'v-input',
    props: {
        label: {
            type: String
        },
        type: {
            type: String,
            default: 'text'
        },
        placeholder: {
            type: String,
            default: '...'
        },
        icon: {
            type: Icon
        }
    },
    components: {
        Icon
    },
    data() {
        return {
            showError: false
        }
    },
    created() {
        this.showError = !Object.values(AvailableTypes).includes(this.type)
    }
}
</script>

<style scoped>
.v-input {
    width:100%;
    display: flex;
    align-items: center;
}
.v-input__type-error {
    text-align: center;
    background-color:rgb(255, 0, 0);
}
input {
    width: inherit;
}
</style>