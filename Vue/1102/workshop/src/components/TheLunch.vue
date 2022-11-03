<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="[toggleShow(), LunchPick()]">Pick One</button>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'TheLunch',
  data: function () {
    return {
        menu: ['국밥','짜장면','햄버거'],
        pick: '',
        show: false,
    }
  },
  methods: {
    LunchPick: function () {
        this.pick = _.sample(this.menu)
        this.$emit('lunch-pick', this.pick, this.show)
    },
    toggleShow: function() {
      if (this.show == false) {
        this.show = true
      }
    }
  }
}
</script>

<style>

</style>