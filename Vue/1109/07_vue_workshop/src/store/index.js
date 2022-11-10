import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    menu: null,
    menus: ['비빔냉면', '짜장면', '볶음밥'],
    lottoNum: null,
    numbers: _.range(1, 46)
  },
  getters: {
  },
  mutations: {
    pickLunch(state) {
      state.menu = _.sample(state.menus)
    },
    lottoPick(state) {
      state.lottoNum = _.sampleSize(state.numbers, 6)
    },
    LUNCHRESET(state) {
      state.menu = null
    }
  },
  actions: {
  },
  modules: {
  }
})
