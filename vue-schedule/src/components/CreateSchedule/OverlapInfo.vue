<template>
<div class="overlap-info">
    <div class="overlap-info__title">
        <icon icon_name="icon-warning" font_size="25"/>
        <span>Произошло наложение</span>
    </div>
    <div class="overlap-info__content">
        <div class="overlap-info-wrapper">
            <view-lesson-card :withTitle="false" :with-stats="false" :slider="false"/>
        </div>
        <div class="overlap-info__separator">
            <span class="horizontal-line horizontal-line--left-border"></span>
            <span>Конфликтует с</span>
            <span class="horizontal-line horizontal-line--right-border"></span>
        </div>
        <div class="overlap-info-wrapper">
            <div class="overlap-info__conflict-list menu">
                <div class="conflict-list__item">
                    <div class="item__title">
                        <div class="menu__item--standart">
                            <v-button :iconName="'icon-info'" :font-size="25"/>
                            <div class="drop-menu drop-menu--left">
                                <p>Напраление: ПИ</p>
                                <p>Группа: ПИ-4ИВТ186А</p>
                                <p>Учебный день: 1</p>
                                <p>Номер пары: 1</p>
                            </div>
                        </div>
                        <span>Курс: 4</span>
                    </div>
                    <div class="conflict-list__item-group">
                        <view-lesson-card :withTitle="false" :withStats="false" :slider="false"/>
                        <view-lesson-card :withTitle="false" :withStats="false" :slider="false"/>
                    </div>
                </div>
                <div class="conflict-list__item">
                    <div class="item__title">
                        <v-button :iconName="'icon-info'" :font-size="25"/>
                        <span>Курс: 4</span>
                    </div>
                    <view-lesson-card :withTitle="false" :withStats="false" :slider="false"/>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import VButton from '../VButton.vue'
import ViewLessonCard from './ViewLessonCard.vue'
export default {
  components: { VButton, ViewLessonCard },

}
</script>

<style scoped>
.overlap-info {
    background-color:burlywood;
}
.overlap-info__title {
    display: flex;
    align-items: end;
    gap: 5px;
}
.overlap-info__content {
    margin-top: 12px;
}
.overlap-info-wrapper {
    padding: 0 10px;
}
.overlap-info__separator {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 4px;
}
.horizontal-line {
    height: 3px;
    background-color: black;
    flex-grow: 1;
}
.horizontal-line--left-border {
    border-radius: 1.5px 0 0 1.5px;
}
.horizontal-line--right-border {
    border-radius: 0 1.5px 1.5px 0;
}
.overlap-info__conflict-list {
    display: flex;
    flex-direction: column;
    gap: 18px;
}
.conflict-list__item-group {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.item__title {
    display: flex;
    align-items: end;
    gap: 8px;
    margin-bottom: 8px;
}
.conflict-list__item {
    width: min-content;
}
</style>