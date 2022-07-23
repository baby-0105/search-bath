<template>
  <header class="flex justify-between p-4">
    <div class="">ちかくのおふろ</div>
    <img class="w-6" src="./assets/img/search.svg" alt="虫眼鏡">
  </header>
  <BathMap></BathMap>
</template>

<script>
import BathMap from './components/BathMap.vue'

export default {
  name: 'App',
  components: {
    BathMap
  }
}
</script>

<style scoped lang="sass">

</style>
