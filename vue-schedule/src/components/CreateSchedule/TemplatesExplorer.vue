<template>
    <div class="temps-explorer">
        <div class="temps-explorer__title">
            <span>Шаблоны</span>
            <div class="temps-explorer__file-actions">
                <icon icon_name="icon-new_folder" font_size="20"/>
                <icon icon_name="icon-trash_bin" font_size="20"/>
            </div>
        </div>
        <div class="open-folder">
            <icon icon_name="icon-go_back" font_size="19"/>
            <div class="open-folder__current-path">
                <span>Папка А</span>
                <icon icon_name="icon-arrow_right" font_size="10"/>
            </div>
        </div>
        <ul class="temps-explorer__list">
            <li v-for="i in 5" :key="i">
                <icon-label icon_name="icon-folder" font_size="20">
                    <span>Папка с шаблонами {{ i }}</span>
                </icon-label>
            </li>
            <li v-for="i in 5" :key="i">
                <icon-label icon_name="icon-template" font_size="20">
                    <span>Шаблон {{ i }}</span>
                </icon-label>
                <icon icon_name="icon-edit" font_size="15"/>
            </li>
        </ul>
    </div>
</template>

<script>
import IconLabel from '../IconLabel.vue'
export default {
  components: { IconLabel },

}
</script>

<style scoped>
ul {
    padding: 0;
    margin: 0;
    list-style-type: none;
}
.temps-explorer {
    background-color: bisque;
}
.temps-explorer__title {
    display: flex;
    justify-content: space-between;
}
.temps-explorer__file-actions {
    display: flex;
    gap: 5px;
}
.open-folder {
    display: flex;
    align-items: center;
    gap: 5px;
}
.open-folder__current-path {
    display: flex;
    align-items: center;
    gap: 5px;
}
.temps-explorer__list {
    background-color: cadetblue;
}
.temps-explorer__list>li {
    display: flex;
    align-items: center;
    gap: 10px;
}
</style>