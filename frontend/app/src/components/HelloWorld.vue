<template>
  <h1>お風呂 {{ message }}</h1>
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
      this.getContents()
        .then((response) => {
          this.message = response.data.message
        })
        .catch((e) => {
          console.log('e:', e);
        })
    },
    methods: {
      getContents() {
        return axios.get('api/hoge')
      }
    },
}
</script>
