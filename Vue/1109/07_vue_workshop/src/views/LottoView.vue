<template>
  <div>
    <h1>{{ menu }}먹고 Lotto 추첨</h1>
    <button @click="lottoPick">Pick Numbers</button>
    <h3>{{ lottoNum }}</h3>
    <button @click="goToHome">처음으로</button>
  </div>
</template>

<script>
export default {
  name: 'LottoView',
  data() {
    return {
        menu: this.$route.params.menu
    }
  },
  methods: {
    lottoPick() {
        this.$store.commit('lottoPick')
    },
    goToHome() {
        this.$router.push({name: 'lunch'})
        this.$store.commit('LUNCHRESET')
    }
  },
  computed: {
    lottoNum() {
        return this.$store.state.lottoNum
    }
  }

}
</script>

<style>

</style>