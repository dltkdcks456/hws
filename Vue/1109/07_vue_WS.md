![image-20221110220234962](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221110220234962.png)



![image-20221110220248057](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221110220248057.png)

- router를 만들어서 lunch와 lotto에 관한 경로를 작성해준다.

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import LunchPage from '@/views/LunchPage'
import LottoPage from '@/views/LottoPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunch',
    component: LunchPage
  },
  {
    path: '/lotto/:menu',
    name: 'lotto',
    component: LottoPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```

- store에는 메뉴에 대한 랜덤을 돌릴 데이터와 로또 숫자를 랜덤하게 뽑을 데이터를 작성하고 각각의 정보를 담을 변수를 설정한다.

```js
import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)
import _ from 'lodash'


export default new Vuex.Store({
  state: {
    menus: ['비빔냉면', '볶음밥', '짜장면'],
    menu: null,
    nums: _.range(1, 46),
    lottoNum: null,
  },
  getters: {
  },
  mutations: {
    PICKLUNCH(state) {
      state.menu = _.sample(state.menus)
    },
    PICKLOTTO(state) {
      state.lottoNum = _.sampleSize(state.nums, 6)
    },
    RESETMENU(state) {
      state.menu = null
    }
  },
  actions: {
  },
  modules: {
  }
})

```



- LottoPage뷰에 Lotto와 관련된 함수를 작성한다. 클릭 시 데이터가 vuex를 통해 전달되고 받아지면서 다른 버튼이 생성된다.

```vue
<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <div v-if="menu">
      <h3>{{ menu }}</h3>
      <button @click="goToLotto">Lotto 뽑으러 가기</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LunchPage',
  computed: {
    menu() {
      return this.$store.state.menu
    },
    
  },
  methods: {
    pickLunch() {
      this.$store.commit('PICKLUNCH')
    },
    goToLotto() {
      this.$router.push({name: 'lotto', params: {menu: this.menu}})
    }
  }
}
</script>

```

- Lotto또한 Lunch와 비슷한 방식으로 작성한다.

```vue
<template>
  <div>
    <h1>{{ menu }} 먹고 Lotto 추첨</h1>
    <button @click="Lottopick">Pick Numbers</button>
    <div v-if="lottoNum">
        <h3>{{ lottoNum }}</h3>
        <button @click="goToLunch">처음으로</button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'LottoPage',
  computed: {
    menu() {
      return this.$route.params.menu
    },
    lottoNum() {
      return this.$store.state.lottoNum
    }
  },
  methods: {
    Lottopick() {
      this.$store.commit('PICKLOTTO')
    },
    goToLunch() {
      this.$store.commit('RESETMENU')
      this.$router.push({name: 'lunch'})
    }
  }
}
</script>
```

