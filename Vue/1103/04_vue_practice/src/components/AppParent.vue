<template>
    <div id="parent">
      <h1>AppParent</h1>
      <input type="text" v-model="parentData" @input="parentToApp">
      <p>appData: {{ appData }}</p>
      <p>childData: {{ childToParent }}</p>
      <AppChild :app-data="appData" :parent-data="parentData" @child-to-parent="ChildToParent"/>
    </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  props: {
    appData: String,
  },
  components: {
    AppChild,
  },
  methods: {
    parentToApp: function () {
        this.$emit('parent-to-app', this.parentData)
    },
    ChildToParent: function(data) {
        this.childToParent = data
        this.$emit('child-to-app', this.childToParent)
    }
  },
  data() {
    return {
        parentData: null,
        childToParent: null,
    }
  }
}
</script>

<style>
#parent {
    border: 1px solid red;
}
</style>