<template>
  <div class="container">
  <!-- Book list container -->
  <div v-for="(book, idx) in books" :key="idx" class="d-flex flex-row card p-5 mb-3">
    <div class="d-flex flex-col"> Book Title: {{ book.title }}</div>
    <div class="d-flex flex-col ml-3">Author: {{ book.author.name }}</div>
    <div class="d-flex flex-col ml-3">ISBN: {{ book.ISBN }}</div>
    <div class="d-flex ml-auto">
      <button type="button" class="btn btn-primary">
        GET BOOK
        <br/>
        Stock: {{ book.stock_count }}
      </button>
      <button type="button" class="btn btn-danger ml-3">
        DELETE
      </button>
      <button type="button" class="btn btn-warning ml-3">
        EDIT
      </button>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'

const API = 'http://localhost:8000'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default {
  name: 'booksearch',
  data () {
    return {
      books: null
    }
  },
  async created() {
    this.searchBooks(this.$route.params.q)
  },
  methods: {
    async searchBooks(q) {
      try {
        const response = await axios.post(`${API}/api/books/search/`, {
          query: q
        }, { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.data.length > 0) {
          this.books = response.data
        }
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>
