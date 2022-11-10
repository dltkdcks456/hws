<template>
  <div>
    <button @click="pickLunch">Pick Lunch</button>
    <div v-if="menu">
      <h3>{{ menu }}</h3>
      <button @click="goToLotto">Lotto 뽑으러가기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "LunchPage",
  computed: {
    menu() {
      return this.$store.state.menu
    }
  },
  methods: {
    pickLunch() {
      this.$store.commit('pickLunch')
    },
    goToLotto() {
      this.$router.push({name:'lotto', params: {menu: this.menu}})
    }
  }
}
</script>

<style>

</style>