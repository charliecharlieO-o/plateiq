<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
  <router-link :to="{name: 'home'}" class="navbar-brand">Small Library</router-link>
  <button class="navbar-toggler" type="button" data-toggle="collapse"
    data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
    aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link :to="{name: 'books'}" class="nav-link">Books</router-link>
      </li>
      <li class="nav-item">
        <router-link :to="{name: 'authors'}" class="nav-link">Authors</router-link>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input v-model="searchQuery" class="form-control mr-sm-2" type="search" placeholder="Search Book Title" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit" @click="search()">
        Search
      </button>
    </form>
  </div>
</nav>
</template>

<script>
export default {
  name: 'navbar',
  data () {
    return {
      searchQuery: null
    }
  },
  methods: {
    search() {
      this.$router.push({ name: 'search', params: { q: this.searchQuery }})
    }
  }
}
</script>

<style scoped>
</style>
