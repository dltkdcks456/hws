<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="AppNum">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childToApp }}</p>
    <AppParent :app-data="AppNum" @parent-to-app="ParentToApp" @child-to-app="ChildToApp"/>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'


export default {
  name: 'App',
  components: {
    AppParent,
    
  },
  data: function() {
    return {
      AppNum: null,
      parentData: null,
      childToApp: null,
    }
  },
  methods: {
    ParentToApp: function(data) {
      this.parentData = data
    },
    ChildToApp: function(data) {
      this.childToApp = data
    }
  }
}
</script>

<style>
#app {
  margin-top: 60px;
  text-align: center;
  border: 1px solid gray;
}
</style>
