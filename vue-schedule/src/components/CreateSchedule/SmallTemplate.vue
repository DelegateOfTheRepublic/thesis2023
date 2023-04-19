<template>
    <div class="template-obj">
        <icon icon_name="icon-template" font_size="35"/>
        <span class="template-obj__hint">
            <icon icon_name="icon-btn-e" font_size="20"/>
            <icon icon_name="icon-down_arrow" font_size="18"/>
            <icon icon_name="icon-edit" font_size="20"/>
        </span>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.template-obj {
    display: flex;
    gap: 5px;
    align-items: center;
    background-color: bisque;
}
.template-obj__hint {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>