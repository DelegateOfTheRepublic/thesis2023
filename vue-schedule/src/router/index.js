import Vue from 'vue'
import Router from 'vue-router'
import LoginForm from '@/components/LoginForm'
import ScheduleView from '@/components/ScheduleView'
import CreateSchedule from '@/components/CreateSchedule'
import Profile from '@/components/Profile'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginForm,
      meta: {
        guest: true
      }
    },
    {
      path: '/schedule',
      name: 'schedule-view',
      component: ScheduleView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/create_schedule',
      name: 'create-schedule',
      component: CreateSchedule,
      meta: {
        requiresAuth: true,
        is_admin: true
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
      meta: {
        requiresAuth: true
      },
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('token') == null) {
      next({
        path: '/login',
        params: { nextUrl: to.fullPath }
      })
    } else {
      let user = JSON.parse(localStorage.getItem('user'))
      if (to.matched.some(record => record.meta.is_admin)) {
        if(user.role == 'Администратор'){
          next()
        } else {
          next({ name: 'create-schedule'})
        }
      } else {
        next()
      }
    }
  } else {
    next()
  }
})

/*} else if (to.matched.some(record => record.meta.guest)) {
  console.log('guest')
  if(localStorage.getItem('token') == null){
    next()
  }
  else{
    next({ name: 'login'})
  }*/

export default router
