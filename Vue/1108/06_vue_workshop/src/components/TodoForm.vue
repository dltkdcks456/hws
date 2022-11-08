<template>
  <div id="me">
    <input 
    type="text"
    v-model.trim="inputText"
    @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
        inputText: null,
    }
  },
  methods: {
    createTodo() {
        if (this.inputText) {
          this.$store.dispatch('createTodo', this.inputText)
        }
        this.inputText = null
    }
  }
}
</script>

<style>

input {
    margin: 15px;
}
</style>