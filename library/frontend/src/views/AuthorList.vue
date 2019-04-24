<template>
  <div class="bookIdx">
    <h1 class="mb-4">Add, Edit and Remove New Authors</h1>

    <!-- Author insertion -->
    <div class="d-flex flex-row justify-content-center mb-3">
      <form class="form-inline">
        <div class="form-group mx-sm-3 mb-2">
          <label for="authorName" class="mr-2">Author Name:</label>
          <input v-model="newAuthor" type="text" class="form-control" id="authorName" placeholder="Complete Name">
        </div>
        <button type="submit" class="btn btn-primary mb-2" @click="postAuthor()">Add Author</button>
      </form>
    </div>

    <!-- Author Index -->
    <div class="container">
      <div v-for="(author, idx) in authors" :key="idx" class="d-flex flex-row card p-5 mb-3">
        <div class="d-flex flex-col">
          <span v-if="inEditId !== idx">{{ author.name }} - Added {{ author.added_on | moment("from") }}</span>
          <input v-else v-model="authors[idx].name" type="text" class="form-control" id="bookTitle" placeholder="New Name">
        </div>
        <div class="d-flex ml-auto">
          <button type="button" class="btn btn-danger ml-3" @click="deleteAuthor(idx, author.id)">
            DELETE
          </button>
          <button v-if="inEditId !== idx" type="button" @click="inEditId = idx" class="btn btn-warning ml-3">
            EDIT
          </button>
          <button v-if="inEditId === idx" type="button" @click="editAuthor(idx, author.id)" class="btn btn-warning ml-3">
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
  name: 'authorlist',
  data () {
    return {
      authors: null,
      newAuthor: '',
      nextPage: null,
      inEditId: null
    }
  },
  created () {
    this.getAuthors()
  },
  methods: {
    async getAuthors () {
      try {
        const response = await axios.get(`${API}/api/authors/`)
        if (response.data.results.length > 0) {
          this.authors = response.data.results
          this.nextPage = response.data.next
        }
      } catch (error) {
        console.log(error)
      }
    },
    async postAuthor () {
      try {
        const response = await axios.post(`${API}/api/authors/`, {
          name: this.newAuthor
        }, { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.status === 201) {
          this.authors.unshift(response.data)
          this.newAuthor = ""
        }
      } catch (error) {
        console.log(error)
      }
    },
    async deleteAuthor (idx, id) {
      try {
        const response = await axios.delete(`${API}/api/authors/${id}`, {
        }, { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.status === 204) {
          this.authors.splice(idx, 1)
        }
      } catch (error) {
        console.log(error)
      }
    },
    async editAuthor (idx, id) {
      try {
        const response = await axios.put(`${API}/api/authors/${id}/`,
          this.authors[idx], { 'Content-Type': 'application/json', 'X-CSRFToken': Cookies.get('csrftoken') })
        if (response.status === 200) {
          this.inEditId = null
        }
      } catch (error) {
        console.log(error)
      }
    },
    async loadMore () {
      try {
        const response = await axios.get(this.nextPage)
        if (response.data.results.length > 0) {
          response.data.results.forEach((e) => {
            this.authors.push(e)
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
