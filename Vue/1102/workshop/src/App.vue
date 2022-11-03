<template>
  <div id="app">
    <TheLunch
      @lunch-pick="TodayLunch"
    />
    <p>{{ todayMenu }}</p>
    <hr>
    <div v-if="Lottoshow">
      <TheLotto :today-menu="todayMenu"/>
    </div>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'
import TheLotto from '@/components/TheLotto'

export default {
  name: 'App',
  components: {
    TheLotto,
    TheLunch
  },
  data: function () {
    return {
      todayMenu: '',
      Lottoshow: null,
    }
  },
  methods: {
    TodayLunch: function(menu, show) {
      this.todayMenu = menu
      this.Lottoshow = show
    }
  },
}
</script>

<style>

</style>
