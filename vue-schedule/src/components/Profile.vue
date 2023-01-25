<template>
    <div class="profile">
        <div class="wrapper">
            <div class="profile-title">
                <div class="avatar">
                    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="50" height="50" x="0" y="0" viewBox="0 0 682.667 682.667" style="enable-background:new 0 0 512 512" xml:space="preserve" class="">
                        <g>
                            <defs>
                                <clipPath id="a" clipPathUnits="userSpaceOnUse">
                                    <path d="M0 512h512V0H0Z" fill="#000000" data-original="#000000"></path>
                                </clipPath>
                            </defs>
                            <g clip-path="url(#a)" transform="matrix(1.33333 0 0 -1.33333 0 682.667)">
                                <path d="M0 0c-44.11 0-80 35.89-80 80s35.89 80 80 80 80-35.89 80-80S44.11 0 0 0Z" style="stroke-width:20;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10;stroke-dasharray:none;stroke-opacity:1" transform="translate(256 236)" fill="none" stroke="#000000" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-dasharray="none" stroke-opacity="" data-original="#000000" class=""></path>
                                <path d="M0 0c.01.13.02.26.04.39 7.25 76.08 71.329 135.58 149.31 135.58 77.98 0 142.049-59.49 149.32-135.57" style="stroke-width:20;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10;stroke-dasharray:none;stroke-opacity:1" transform="translate(106.65 60.03)" fill="none" stroke="#000000" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-dasharray="none" stroke-opacity="" data-original="#000000" class=""></path>
                                <path d="M0 0c0-5.523-4.478-10-10-10S-20-5.523-20 0s4.478 10 10 10S0 5.523 0 0" style="fill-opacity:1;fill-rule:nonzero;stroke:none" transform="translate(450 420)" fill="#000000" data-original="#000000"></path>
                                <path d="M0 0c22.581-37.189 35.579-80.857 35.579-127.592 0-79.79-37.89-150.65-96.68-195.57v-.01c-41.39-31.64-93.14-50.42-149.32-50.42-56.17 0-107.92 18.78-149.309 50.42-58.791 44.92-96.691 115.78-96.691 195.58 0 135.96 110.02 246 246 246 56.871 0 109.207-19.25 150.851-51.598" style="stroke-width:20;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10;stroke-dasharray:none;stroke-opacity:1" transform="translate(466.42 383.592)" fill="none" stroke="#000000" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-dasharray="none" stroke-opacity="" data-original="#000000" class=""></path>
                            </g>
                        </g>
                    </svg>
                </div>
                <p>Елисей Л. Н.</p>
            </div>
        </div>
        <div class="profile-info">
            <div class="fio">
                <label for="">Статус:</label>
                <p>Студент</p>
            </div>
            <div>
                <label for="">Номер телефона:</label>
                <p>+78889997654</p>
            </div>
            <div>
                <label for="">Email:</label>
                <p>myemail@mail.ru</p>
            </div>
            <div>
                <label for="">Должность:</label>
                <p>Доцент</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.profile{
    width: 350px;
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}

.wrapper{
    padding: 15px;
    border-bottom: 2px solid gainsboro;
}

.profile-title{
    width: 55%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: auto;
}

.profile-info{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    flex-grow: 0.5;
    padding: 15px;
}

.profile-info>div{
    display: flex;
    justify-content: space-between;
}

p{
    margin: 0;
    pointer-events: none;
}
</style>