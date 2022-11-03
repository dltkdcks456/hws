<template>
  <div>
    <h1>{{ todayMenu }} 먹고 로또</h1>
    <button @click="GetLotto">Get Lucky Numbers</button>
    <p>{{ lottoNum }}</p>
  </div>
</template>


<script>
import _ from "lodash"

export default {
  name: 'TheLotto',
  data: function () {
    return {
        lottoNum: ''
    }
  },
  methods: {
    GetLotto: function() {
        const numList = _.range(1, 46)
        this.lottoNum = _.sampleSize(numList, 6)
    }
  },
  props: {
    todayMenu: String,
  }
}

</script>

<style>

</style>