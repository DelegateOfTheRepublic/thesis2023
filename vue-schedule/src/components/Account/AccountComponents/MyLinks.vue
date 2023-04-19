<template>
    <div class="my-links">
        <div class="my-links__head">
            <span>Мои ссылки</span>
            <div class="menu__item--standart">
                <v-button :iconName="'icon-add_link'" :fontSize="22"/>
                <div class="drop-menu">
                    <div class="add-link__wrapper">
                        <div class="link-group">
                            <span>Группа ссылок:</span>
                            <select name="" id="">
                                <option value="">конференции</option>
                                <option value="">группы</option>
                                <option value="">облака</option>
                                <option value="">связь со мной</option>
                            </select>
                        </div>
                        <div class="link-input">
                            <span>Ссылка:</span>
                            <input type="text" placeholder="Your link..."/>
                        </div>
                        <v-button :iconName="'icon-submit'" :fontSize="19" :title="'Добавить'"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="my-links__list">
            <div class="list__item">
                <span>Конференции</span>
                <div class="list-item__wrapper">
                    <icon-label :icon_name="'icon-zoom'" :font_size="19">Link to Zoom</icon-label>
                    <icon-label :icon_name="'icon-discord'" :font_size="19">Link to Discord</icon-label>
                </div>
            </div>
            <div class="list__item">
                <span>Группы</span>
                <div class="list-item__wrapper">
                    <icon-label :icon_name="'icon-telegram'" :font_size="19">Link to Telegram</icon-label>
                    <icon-label :icon_name="'icon-discord'" :font_size="19">Link to Discord</icon-label>
                    <icon-label :icon_name="'icon-whatsapp'" :font_size="19">Link to Whatsapp</icon-label>
                </div>
            </div>
            <div class="list__item">
                <span>Облака</span>
                <div class="list-item__wrapper">
                    <icon-label :icon_name="'icon-yandex_disk'" :font_size="19">Link to Yandex Disk</icon-label>
                    <icon-label :icon_name="'icon-google_drive'" :font_size="19">Link to Google Drive</icon-label>
                </div>
            </div>
            <div class="list__item">
                <span>Связь со мной</span>
                <div class="list-item__wrapper">
                    <icon-label :icon_name="'icon-telegram'" :font_size="19">Link to Telegram</icon-label>
                    <icon-label :icon_name="'icon-whatsapp'" :font_size="19">Link to Whatsapp</icon-label>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import IconLabel from '../../IconLabel.vue'
import VButton from '../../VButton.vue'

export default {
    components: {
        IconLabel, VButton
    }
}
</script>

<style scoped>
.my-links {
    background-color: bisque;
}
.my-links__head {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.my-links__list {
    margin-top: 15px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 25px;
}
.list__item {
    /*width: fit-content;*/
    background-color: cornflowerblue;
}
.list-item__wrapper {
    margin-top: 10px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.link-group,
.link-input {
    display: flex;
    gap: 5px;
    align-items: center;
    background-color:crimson;
}
.add-link__wrapper {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.add-link__wrapper>div[id='v-button'] {
    margin: 12px auto 0;
}
</style>