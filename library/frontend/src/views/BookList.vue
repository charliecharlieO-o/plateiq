<template>
  <div class="bookIdx">
    <h1 class="mb-4">Add, Edit and Remove New Titles</h1>
    <div class="d-flex flex-row justify-content-center mb-3">
      <form class="form-inline">
        <div class="form-group mx-sm-3 mb-2">
          <label for="authorSelect" class="mr-2">Author:</label>
          <select v-model="selectedAuthor" class="form-control mr-3" id="authorSelect">
            <option v-for="author in authors" v-bind:value="author.id">{{ author.name }}</option>
          </select>
          <label for="bookTitle" class="mr-2">Book Title:</label>
          <input v-model="newTitle" type="text" class="form-control" id="bookTitle" placeholder="BookTitle">
          <label for="bookISBN" class="ml-2 mr-2">ISBN:</label>
          <input v-model="newISBN" type="text" class="form-control" id="bookISBN" placeholder="ISBN">
        </div>
        <button type="submit" class="btn btn-primary mb-2" @click="postBook()">Add Book</button>
      </form>
    </div>
    <!-- Book list container -->
    <div class="container">
      <div v-for="(book, idx) in books" :key="idx" class="d-flex flex-row card p-5 mb-3">
        <div class="d-flex flex-col">
          <span v-if="inEditId !== idx">Book Title: {{ book.title }}</span>
          <input v-else v-model="books[idx].title" type="text" class="form-control" placeholder="New Title">
        </div>
        <div class="d-flex flex-col ml-3">Author: {{ book.author.name }}</div>
        <div class="d-flex flex-col ml-3">ISBN: {{ book.ISBN }}</div>
        <div class="d-flex ml-auto">
          <button type="button" class="btn btn-primary">
            GET BOOK
            <br/>
            Stock: {{ book.stock_count || '0' }}
          </button>
          <button type="button" class="btn btn-danger ml-3" @click="deleteBook(idx, book.id)">
            DELETE
          </button>
          <button v-if="inEditId !== idx" type="button" @click="inEditId = idx" class="btn btn-warning ml-3">
            EDIT
          </button>
          <button v-if="inEditId === idx" type="button" @click="editBook(idx, book.id)" class="btn btn-warning ml-3">
            SAVE
          </button>
        </div>
      </div>
      <div class="d-flex flex-row justify-content-center">
        <button v-if="nextPage !== null" @click="loadMore()" class="btn btn-primary mb-3">LOAD MORE</button>
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
  name: 'booklist',
  data () {
    return {
      books: null,
      nextPage: null,
      authors: null,
      inEditId: null,
      selectedAuthor: null,
      newTitle: "",
      newISBN: ""
    }
  },
  async created() {
    this.getBooks()
    this.getAllAuthors()
  },
  methods: {
    async getBooks () {
      try {
        const response = await axios.get('http://localhost:8000/api/books')
        if (response.data.results.length > 0) {
          this.books = response.data.results
          this.nextPage = response.data.next
        }
      } catch (error) {
        console.log(error)
      }
    },
    async getAllAuthors () {
      try {
        const response = await axios.get('http://localhost:8000/api/authors/all/')
        if (response.data.length > 0) {
          this.authors = response.data
        }
      } catch (error) {
        console.log(error)
      }
    },
    async deleteBook (idx, id) {
      try {
        const response = await axios.delete(`${API}/api/books/${id}/`, {
        }, { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.status === 204) {
          this.books.splice(idx, 1)
        }
      } catch (error) {
        console.log(error)
      }
    },
    async editBook (idx, id) {
      try {
        let book = this.books[idx]
        book.author = book.author.id
        const response = await axios.put(`${API}/api/books/${id}/`,
          book, { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.status === 200) {
          this.inEditId = null
        }
      } catch (error) {
        console.log(error)
      }
    },
    async postBook () {
      try {
        console.log(this.selectedAuthor)
        const response = await axios.post(`${API}/api/books/`, {
          title: this.newTitle,
          author: this.selectedAuthor,
          ISBN: this.newISBN
        }, { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.status === 201) {
          this.books.unshift(response.data)
        }
      } catch (error) {
        console.log(error)
      }
    },
    async loadMore () {
      try {
        const response = await axios.get(this.nextPage)
        if (response.data.count > 0) {
          response.data.results.forEach((e) => {
            this.books.push(e)
          })
          this.nextPage = response.data.next
        }
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>
