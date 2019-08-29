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
      path: '/edit',
      name: 'edit',
      component: () => import('./views/Editor.vue')
    },
    {
      path: '/books',
      name: 'books',
      component: () => import('./views/NoteBook.vue')
    },
    {
      path: '/drafts',
      name: 'drafts',
      component: () => import('./views/Drafts.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./views/Register.vue')
    },
    {
      path: '/view/:noteid',
      name: 'view',
      component: () => import('./views/ViewNote.vue')
    },
    {
      path: '/recycle',
      name: 'recycle',
      component: () => import('./views/Recycle.vue')
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
