<template>
    <div>
      <span id="btn" @click="updateTodoStatus"
      :class="{'is_completed': todo.isCompleted}"
      >
      {{ todo.title }}
    </span>
      <button @click="deleteTodo">Delete</button>
    </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object
  },
  methods: {
    deleteTodo() {
        this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodoStatus() {
        this.$store.dispatch('updateTodoStatus', this.todo)
    }
  }
}
</script>

<style>
button {
  margin: 5px;
}
.is_completed {
    text-decoration: line-through;
    color: grey;
}
#btn {
    cursor: pointer;
}
</style>