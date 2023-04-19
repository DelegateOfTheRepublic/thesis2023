<template>
<div class="toolbar">
    <div class="toolbar__selection-info">
        <icon icon_name="icon-checkbox" :font_size="btnsFontSize"><p>{{pickedElements}} элемент</p></icon>
    </div>
    <ul class="toolbar__btns menu">
        <li class="menu__item">
            <v-button :iconName="'icon-edit'" :fontSize="btnsFontSize" :title="'Изменить'"/>
            <ul class="drop-menu">
                <li class="drop-menu__item">
                    <v-button :iconName="'icon-eye'" :fontSize="'17'" :title="'Показывать оригинал'"/>
                </li>
            </ul>
        </li>
        <li class="menu__item">
            <v-button :iconName="'icon-save'" :fontSize="btnsFontSize" :title="'Сохранить'"/>
            <ul class="drop-menu">
                <li class="drop-menu__item">
                    <v-button :iconName="'icon-save_full'" :fontSize="'15'" :title="'Полностью'"/>
                </li>
                <li class="drop-menu__item">
                    <v-button :iconName="'icon-save_split'" :fontSize="'15'" :title="'По-отдельности'"/>
                </li>
            </ul>
        </li>
        <li><v-button :iconName="'icon-duplicate'" :fontSize="btnsFontSize" :title="'Дублировать'"/></li>
        <li><v-button :iconName="'icon-clear'" :fontSize="btnsFontSize" :title="'Очистить'"/></li>
        <li><v-button :iconName="'icon-linking'" :fontSize="btnsFontSize" :title="'Связать'"/></li>
    </ul>
</div>
</template>

<script>
import vButton from '../VButton.vue'

export default {
    components: {
        vButton
    },
    data() {
        return{
            btnsFontSize: 19,
            pickedElements: '1'
        }
    }
}
</script>

<style scoped>
.toolbar {
    display: flex;
    gap: 154px;
}

.toolbar__selection-info>div {
    align-items: center;
}

.toolbar__btns {
    display: flex;
    gap: 15px;
}
</style>