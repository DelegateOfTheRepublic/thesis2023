<template>
    <nav>
        <div class="container menu">
            <div class="nav__logo"><a href="https://bashedu.ru/" target="_blank">LOGO</a></div>
            <div class="nav__usefule-resources">
                <a href="https://sdo.bashedu.ru/login/index.php" target="_blank">перейти в СДО</a>
                <a href="https://cabinet.bashedu.ru/" target="_blank">перейти в ЛК</a>
            </div>
            <div class="nav__navigation">
                <div class="nav__notifications">
                    <div class="menu__item--standart">
                        <v-button :iconName="'icon-bell'" :fontSize="25"/>
                        <div class="notifications__list drop-menu">
                            <div class="notification">
                                <icon icon_name="icon-avatar" font_size="25"/>
                                <icon icon_name="icon-arrow_right" font_size="12"/>
                                <span>Студент добавил д/з</span>
                            </div>
                            <div class="notification">
                                <icon icon_name="icon-avatar" font_size="25"/>
                                <icon icon_name="icon-arrow_right" font_size="12"/>
                                <span>Студент загрузил файл</span>
                            </div>
                            <div class="notification">
                                <icon icon_name="icon-telegram" font_size="25"/>
                                <icon icon_name="icon-arrow_right" font_size="12"/>
                                <span>Загружен новый файл</span>
                            </div>
                        </div>
                    </div>
                    <div class="menu__item--standart">
                        <v-button :iconName="'icon-advert'" :fontSize="25"/>
                        <div class="adverts__list drop-menu">
                            <p>Объявление АБС</p>
                            <p>Объявление АБСССС</p>
                            <p>Объявление 1</p>
                        </div>
                    </div>
                </div>
                <div class="nav__list">
                    <div class="nav__link">
                        <span>Файлы</span>
                    </div>
                    <div class="nav__link">
                        <span>Просмотр расписания</span>
                    </div>
                    <div class="menu__item--standart">
                        <v-button :iconName="'icon-arrow'" :fontSize="10" :title="'Домашние задания'" :iconPosition="'right'"/>
                        <div class="drop-menu">
                            <div class="homeworks__list">
                                <p>Нейроинформатика</p>
                                <p>Теория игр и исследование операций</p>
                            </div>
                        </div>
                    </div>
                    <v-button :iconName="'icon-online_lesson'" :fontSize="15" :title="'Пара А'" :iconPosition="'right'"/>
                </div>
            </div>
            <div class="nav__profile">
                <icon icon_name="icon-avatar" font_size="40"/>
                <div class="menu__item--standart">
                    <v-button :iconName="'icon-arrow'" :fontSize="15" :title="'Антон В.Б.'" :iconPosition="'right'"/>
                    <div class="drop-menu">
                        <div class="profile-menu">
                            <v-button :iconName="'icon-arrow_right'" :fontSize="10" :title="'Личный кабинет'" :iconPosition="'right'"/>
                            <v-button :iconName="'icon-door'" :fontSize="20" :title="'Выход'"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import Icon from './Icon.vue'
import IconLabel from './IconLabel.vue'
import VButton from './VButton.vue'
export default {
  components: { Icon, VButton, IconLabel },

}
</script>

<style scoped>
nav {
    width: 100%;

    background-color: cadetblue;
}
.container {
    width: 1180px;
    height: 46px;
    margin: auto;
    display: flex;

    align-items: center;

    background-color: bisque;
}
.nav__logo {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 76px;
    height: 100%;
    color: white;
    background-color: black;
}
.nav__usefule-resources {
    display: flex;
    flex-direction: column;;
    margin-left: 20px;
    font-size: 12px;
    gap: 6px;
}
.nav__usefule-resources > a {
    border-left: 3px solid lime;
}
.nav__navigation {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-grow: 1;
    height: 100%;
}
.nav__notifications {
    display: flex;
    gap: 8px;
    margin-right: 12px;
}
.notifications__list {
    min-width: 250px;
}
.notification {
    display: flex;
    align-items: center;
    gap: 2px;
    padding: 5px 0;
}
.adverts__list {
    width: 200px;
}
.adverts__list > p {
    padding: 5px 0;
}
.nav__list {
    display: flex;
    gap: 14px;
}
.nav__select {
    display: flex;
    align-items: center;
}
.nav__link {
    display: flex;
    align-items: center;
    gap: 4px;
}
.nav__profile {
    display: flex;
    align-items: center;
    height: 100%;
}
.profile-menu {
    width: 250px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    transform: translateX(-18%);
    margin-top: 5px;
}
.homeworks__list {
    width: 240px;
    word-wrap: break-word;
}
.homeworks__list > p {
    padding: 5px 0;
}
</style>
