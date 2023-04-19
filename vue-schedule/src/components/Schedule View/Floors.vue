<template>
<div class="floors">
    <div v-for="i in 3" :key="i" class="floor">
        <p>{{floor_number}}-й этаж</p>
        <div class="floor__audits">
            <p v-for="audit_number in auditories" :key="audit_number">{{audit_number}}</p>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{
            floor_number: '5',
            auditories: ['530', '515', '524', '525', '530', '515', '524', '525',
                         '530', '515', '524', '525', '530', '515', '524', '525',
                         '530', '515', '524', '525', '530', '515', '524', '525']
        }
    }
}
</script>

<style scoped>

.floors {
    width: fit-content;
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 15px;
    background-color:cornflowerblue;
}

.floor {
    text-align: center;
}

.floor__audits {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    gap: 10px;
    margin-top: 5px;
    background-color:bisque;
}

p{
    margin: 0;
}
</style>