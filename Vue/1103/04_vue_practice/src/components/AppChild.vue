<template>
    <div id="child">
      <h1>AppChild</h1>
      <input type="text" v-model="childData" @input="ChildToParent">
      <p>appData: {{ appData }}</p>
      <p>parentData: {{ parentData }}</p>
      <p>childData: {{ childData }}</p>
    </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: String,
    parentData: String,
  },
  data: function () {
    return {
        childData: null,
    }
  },
  methods: {
    ChildToParent: function() {
        this.$emit('child-to-parent', this.childData)
    }
  }
}
</script>

<style>
#child {
    border: 1px solid blue;
}
</style>