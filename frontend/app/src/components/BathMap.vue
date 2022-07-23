<template>
  <div class="flex">
    <ul class="w-1/4 overflow-auto h-screen border-r-2">
      <li class="flex justify-between p-3 border-b-2">
        <img src="../assets/img/arugo.svg" alt="お風呂画像">
        <div class="text-center">
          <h3 class="text-lg mb-1">あるごの湯</h3>
          <div class="place text-sm text-slate-600 mb-1">大阪府豊中市豊津町</div>
          <div class="time text-sm text-slate-600 mb-1">10:00 ~ 25:00</div>
          <button class="text-sm border rounded-full p-2 bg-cyan-400">クリックで詳細表示</button>
        </div>
      </li>
    </ul>
    <div>MAPエリア</div>
  </div>
</template>

<script></script>

<style scoped lang="sass">
  @mixin pseudo-icon($url, $width: 20px)
    display: flex
    justify-content: between
    &::before
      content: ""
      background: url("../assets/#{$url}")
      background-size: contain
      background-repeat: no-repeat
      background-position: 50% 50%
      display: inline-block
      width: $width

  .place
    @include pseudo-icon("img/map_pin.svg")
    &::before
      margin-right: 20px

  .time
    @include pseudo-icon("img/time.svg")
    &::before
      margin-right: 20px
</style>
