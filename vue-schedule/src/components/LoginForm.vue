<template>
<div>
    <form action="" class="login-form">
        <div>
            <label for="">Email
            <input type="email" name="" id="" required>
            </label>
        </div>
        <div>
            <label for="">Password
            <input type="password" name="" id="" required>
            </label>
        </div>
        <input type="submit" value="Login" class="login-button">
    </form>
</div>
</template>

<script>

</script>

<style scoped>
.login-form{
  width: fit-content;
  margin: auto;
  height: 120px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid rgb(238, 238, 238);
  border-radius: 10px;
  box-shadow: 4px 4px 10px 0px rgba(34, 60, 80, 0.2);
}

.login-button{
  width: fit-content;
  padding: 3px;
  padding-left: 7px;
  padding-right: 7px;
  margin: auto;
  margin-top: 0;
  margin-bottom: 0;
}
</style>
