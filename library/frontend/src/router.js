import Vue from 'vue'
import Router from 'vue-router'
import AuthorList from './views/AuthorList.vue'
import BookList from './views/BookList.vue'
import SearchBook from './views/SearchBook.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: BookList
    },
    {
      path: '/authors',
      name: 'authors',
      component: AuthorList
    },
    {
      path: '/books',
      name: 'books',
      component: BookList
    },
    {
      path: '/search/:q',
      name: 'search',
      component: SearchBook
    }
  ]
})
