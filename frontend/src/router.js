import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
// import EditNote from "./views/EditNote.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue')
    },
    {
      path: '/view/:noteid',
      name: 'view',
      component: () => import('./views/ViewNote.vue')
    },
    {
      path: '/center/books',
      name: 'books',
      component: () => import('./views/center/Books.vue')
    },
    {
      path: '/center/recycle',
      name: 'recycle',
      component: () => import('./views/center/Recycle.vue')
    },
    {
      path: '/center/edit',
      name: 'edit',
      component: () => import('./views/center/Editor.vue')
    },
    {
      path: '/center/private',
      name: 'private',
      component: () => import('./views/center/Private.vue')
    },
    {
      path: '/center/drafts',
      name: 'drafts',
      component: () => import('./views/center/Drafts.vue')
    },
    {
      path: '/center/setting',
      name: 'setting',
      component: () => import('./views/center/Setting.vue')
    },
    {
      path: '/center',
      name: 'center',
      component: () => import('./views/center/Center.vue')
    },
    {
      path: '/404',
      name: '404',
      component: () => import('./views/ErrorView.vue')
    },
    {
      path: '*',
      redirect: {
        name: '404'
      }
    }
  ]
})
