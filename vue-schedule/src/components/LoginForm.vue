<template>
<div>
    <form action="" class="login-form">
        <div>
            <label for="">Email
            <input type="email" name="" id="" v-model="email" required>
            </label>
        </div>
        <div>
            <label for="">Password
            <input type="password" name="" id="" v-model="password" required>
            </label>
        </div>
        <input type="submit" value="Login" class="login-button" @click="login">
    </form>
</div>
</template>

<script>
export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  created() {
    if (localStorage.getItem('token')) {
      this.$router.push("/schedule");
    }
  },
  methods: {
    async login(e) {
      e.preventDefault()
      if (this.password.length >= 8) {
        await this.axios.post('http://localhost:8000/api/auth/token/login', {
          'username': this.email,
          'password': this.password
        }).then(response => {
          this.setToken(response.data.auth_token)
          this.getUserProfile()
          this.$router.push("/schedule")
        }).catch(error => {
          console.error(error.response)
        })
      }
    },
    async getUserProfile() {
      await this.axios.get('http://localhost:8000/api/profile/', {
        'headers': {'Authorization': `Token ${localStorage.getItem('token')}`}
      }).then(response => {
          this.setUser(JSON.stringify(response.data.user))
        }).catch(error => {
          console.error(error.response)
        })
    },
    setToken(token) {
      localStorage.setItem('token', token)
    },
    setUser(user) {
      localStorage.setItem('user', user)
    }
  }
}
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
