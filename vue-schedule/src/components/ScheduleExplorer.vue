<template>
    <div class="vertmenu">
        <ul>
            <li>
                <a class="active">Пункт меню 1</a>
                <input type="checkbox" class="subCat" id="1" checked="checked" />

                <ul style="display:none">
                    <li>
                        <a class="active" href="#">Пункт меню 1.1</a>
                        <input type="checkbox" class="subCat" id="1.1" checked="checked"/>
                        <label class="chka" for="1.1"></label>
                        <ul style="display:none">
                            <li>
                                <a>Пункт меню 1.1.1</a>
                            </li>
                            <li>
                                <a href="#">Пункт меню 1.1.2</a>
                            </li>
                            <li>
                                <a href="#">Пункт меню 1.1.3</a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="#">Пункт меню 1.2</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 1.3</a>
                    </li>
                </ul>
            </li>
            <li>
                <a href="#">Пункт меню 2</a>
                <input type="checkbox" class="subCat" id="2" />
                <label class="chka" for="2"></label>
                <ul style="display:none">
                    <li>
                        <a href="#">Пункт меню 2.1</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 2.2</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 2.3</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 2.4</a>
                    </li>
                </ul>
            </li>
            <li>
                <a href="#">Пункт меню 3</a>
                <input type="checkbox" class="subCat" id="3" />
                <label class="chka" for="3"></label>
                <ul style="display:none">
                    <li>
                        <a href="#">Пункт меню 3.1</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 3.2</a>
                    </li>
                </ul>
            </li>
            <li>
                <a href="#">Пункт меню 4</a>
                <input type="checkbox" class="subCat" id="4" />
                <label class="chka" for="4"></label>
                <ul style="display:none">
                    <li>
                        <a href="#">Пункт меню 4.1</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 4.2</a>
                    </li>
                    <li>
                        <a href="#">Пункт меню 4.3</a>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.vertmenu {
margin: 0 20px;
font-family: 'Open Sans', sans-serif;
}
.vertmenu ul {
list-style: none;
margin: 0;
padding: 0;
}
.vertmenu ul li {
position: relative;
margin: 0;
line-height: 30px;
text-transform: uppercase;
}
.vertmenu ul li li {
padding-left:20px;
}
.vertmenu .subCat, .chka {
top: 0;
right: 0px;
position: absolute;
cursor: pointer;
}
.vertmenu .subCat.plus,
.chka:before,
.vertmenu .subCat.minus,
.subCat:checked + .chka:before {
content: '+';
font-size: 26px;
color: #1266B1;
font-weight: bold;
font-family: Courier;
}
.vertmenu .subCat.minus, .subCat:checked + .chka:before {
content: '-';
}
.vertmenu a {
color: #477AB9;
font-size: 16px;
font-weight:bold;
text-decoration:none;
}
.vertmenu ul li li a {
color: #666;
font-size: 15px;
font-weight:normal;
text-decoration:none;
}
.vertmenu a.active {
color: #00B1EC;
}
.vertmenu a:hover {
text-decoration: none;
color: #000 !important;
}
.vertmenu > ul > li ul {
display: none;
}
.vertmenu > ul > li a.active + span + ul {
display: block !important;
}
.vertmenu > ul > li .subCat:checked ~ ul {
display: block !important;
}
.vertmenu input[type=checkbox].subCat {
display:none;
}
.vertmenu ul li li a:before {
content: '\203A';
font-size: 20px;
padding-right: 6px;
color: #666;
font-weight: bold;
}
.vertmenu > ul li li a:hover:before {
color: #1266B1;
}
</style>