<template>
    <div class="add_new_lesson" @click="$emit('click', $event)">
        <p>Добавить пару</p>
    </div>
</template>

<script>
export default {
    emits: []
}
</script>

<style scoped>
.add_new_lesson{
    border: 3px dashed rgba(130, 130, 130, 0.797);
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.2s ease-in-out;
}

.add_new_lesson:hover{
    cursor: pointer;
    background-color: gainsboro;
}

p{
    pointer-events: none;
}
</style>