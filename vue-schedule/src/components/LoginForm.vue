<template>
<div>
    <form action="" class="login-form">
      <div class="current_st_day">
        <div class="cur_st_day-header">
          <div class="cur_st_day-header-week">
            <p>Четная неделя</p>
            <div class="small_vertical_line"></div>
            <p>20-я неделя</p>
          </div>
          <div class="cur_st_day-header-date">
            <p>Вт.</p>
            <div class="small_vertical_line"></div>
            <p>23.02.2023</p>
          </div>
        </div>
        <div class="horizontal_line"></div>
        <div class="cur_st_day-lesson_info">
          <div class="cur_st_day-lesson_info-header">
            <p>1-я пара</p>
            <p>13:40-15:00</p>
          </div>
          <div class="cur_st_day-lesson_info-data">
            <p class="cur_st_day-lesson_info-data-subject">Основы проектной деятельности</p>
            <div class="cur_st_day-lesson_info-data-dates">
              <icon icon_name="icon-calendar"/>
              <p>По 22 н.</p>
            </div>
            <div class="cur_st_day-lesson_info-data-location">
              <icon icon_name="icon-location"/>
              <p>Ауд. 525</p>
            </div>
            <div class="cur_st_day-lesson_info-data-teacher">
              <icon icon_name="icon-teacher"/>
              <div>
                <p>Доц.</p>
                <p>Якшибаева Г.В.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="vertical_line"></div>

      <div class="data_inputs">
        <div class="data_inputs-nav">
          <p>Авторизация</p>
          <div class="small_vertical_line"></div>
          <p>Забыли пароль?</p>
        </div>
        <div class="data_inputs-form">
          <div class="data_inputs-form-inputs">
            <div class="data_inputs-form-inputs-email">
              <div class="data_inputs-form-inputs-email-placeholder icon_placeholder">
                <icon icon_name="icon-email"/>
              </div>
              <input class="data_inputs-form-inputs-email-input" type="email" name="" id=""/>
            </div>
            <div class="data_inputs-form-inputs-password">
              <div class="data_inputs-form-inputs-pwd-placeholder icon_placeholder">
                <icon icon_name="icon-password"/>
              </div>
              <input class="data_inputs-form-inputs-pwd-input" type="password" name="" id=""/>
              <div class="data_inputs-form-inputs-pwd-lock_icon">
                <icon icon_name="icon-lock"/>
              </div>
            </div>
            <div class="data_inputs-form-inputs-remember_me">
              <input type="checkbox" name="" id="">
              <p>Запомни меня</p>
            </div>
          </div>
          <input class="data_inputs-form-login_btn" type="button" value="Login"/>
        </div>
      </div>
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
        this.axios.post('http://localhost:8000/api/auth/token/login', {
          'username': this.email,
          'password': this.password
        }).then(async response => {
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
p{
  margin: 0;
}
</style>