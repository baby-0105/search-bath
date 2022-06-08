<template>
  <div class="hello">
    <h1>Hello World {{ message }}</h1>
  </div>
</template>

<script>
import { axios } from '/app/plugins/axios'

export default {
    components: {
    },
    data() {
      return {
        message : ''
      }
    },
    mounted() {
      this.get_hoge().then((response) =>{
        this.message = response.data.message
      })
    },
    methods: {
      get_hoge() {
        return axios.get('api/hoge')
      }
    },
}
</script>

<style scoped>
h1 {
  color: #42b983;
}
</style>