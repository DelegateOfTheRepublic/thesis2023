import Vue from 'vue'
import Router from 'vue-router'
import LoginForm from '@/components/LoginForm'
import ScheduleView from '@/components/ScheduleView'
import CreateSchedule from '@/components/CreateSchedule'
import Profile from '@/components/Profile'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'LoginForm',
      component: LoginForm
    },
    {
      path: '/schedule',
      name: 'ScheduleView',
      component: ScheduleView
    },
    {
      path: '/create_schedule',
      name: 'CreateSchedule',
      component: CreateSchedule
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    }
  ]
})
