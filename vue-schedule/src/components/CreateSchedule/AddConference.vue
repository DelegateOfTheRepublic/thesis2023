<template>
    <div class="remote-format">
        <span>Конференция</span>
        <div class="remote-format__content">
            <div class="remote-format__platform">
                <span>Платформа:</span>
                <select name="" id="">
                    <option value="">Zoom</option>
                </select>
            </div>
            <span>Ссылка: http://zoom/</span>
            <span>ID: 345 345 34 21</span>
            <span>Код доступа: f34GD</span>
        </div>
        <div class="remote-format__btns">
            <v-button :iconName="'icon-submit'" :fontSize="16"/>
            <v-button :iconName="'icon-cancel'" :fontSize="16"/>
        </div>
    </div>
</template>

<script>
import VButton from '../VButton.vue'
export default {
  components: { VButton },

}
</script>

<style scoped>
.remote-format {
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: center;
    background-color: bisque;
}
.remote-format__content {
    display: flex;
    flex-direction: column;
    gap: 6px;
    background-color: cadetblue;
}
.remote-format__platform {

}
.remote-format__btns {
    display: flex;
    gap: 40px;
}
</style>