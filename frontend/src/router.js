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
      component: Home,
      id: '0'
    },
    {
      path: '/edit',
      name: 'edit',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ './views/Edit.vue')
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
    }
  ]
})
