<template>
    <div class="slider">
        <div class="slider__circle"></div>
        <div class="slider__circle"></div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.slider {
    width: fit-content;
    display: flex;
    align-self: center;
    gap: 10px;
}

.slider__circle{
    width: 10px;
    height: 10px;
    border-radius: 5px;
    background-color: rgb(187, 187, 187);
}
</style>