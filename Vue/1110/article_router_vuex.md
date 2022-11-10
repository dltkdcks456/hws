![image-20221110232620528](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221110232620528.png)

![image-20221110232637313](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221110232637313.png)

![image-20221110232653504](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221110232653504.png)

![image-20221110232717117](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221110232717117.png)

- router를 통해서 각각의 경로를 이어준다.(index, create, 404, detail)

```js
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
import IndexView from '@/views/IndexView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import NotFound404 from '@/views/NotFound404'

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '*',
    redirect: {name: 'NotFound404'}
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```

- store에는 기본적으로 articles에 대한 정보를 적고, create/delete 기능을 추가한다

```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article_id: 3,
    articles: [
      {
        id: 1,
        title: 'title1',
        content: 'content1',
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: 'title2',
        content: 'content2',
        createdAt: new Date().getTime(),
      }
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id += 1
    },
    DELETE_ARTICLE(state, id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === id)
      })
    }
  },
  actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
  modules: {
  }
})

```

- CreateView에는 사용자가 작성할 수 있는 폼을 기록해준다.

```js
<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 :</label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="conten"></label>
      <textarea id="content" cols="30" rows="10" v-model.trim="content"></textarea><br>
      <input type="submit">
    </form>
    <router-link :to="{name: 'index'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요!')
      } else if (!content) {
        alert('내용을 입력해주세요')
      } else {
        const payload = {
          title, content
        }
        this.$store.dispatch('createArticle', payload)
        this.$router.push({name: 'index'})
      }
    }
  }
}
</script>

```

- Detail에는 세부 내용이 표시될 수 있도록 연결시켜준다.

```js
<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{article?.id}}</p>
    <p>글 제목: {{article?.title }}</p>
    <p>글 내용: {{article?.content}}</p>
    <p>작성 시간: {{articleCreatedAt}}</p>
    <button @click="deleteArticle">삭제</button><br>
    <router-link :to="{name: 'index'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
        article: null,
    }
  },
  computed: {
    articles() {
        return this.$store.state.articles
    },
    articleCreatedAt() {
        const article = this.article
        const createdAt = new Date(article?.createdAt).toLocaleString()
        return createdAt
    }
  },
  methods: {
    getArticleById(id) {
        for (const article of this.articles) {
            if (article.id === Number(id)) {
                this.article = article
            }
        }
        if (!this.article) {
            this.$router.push({name: 'NotFound404'})
        }
    },
    deleteArticle() {
        this.$store.commit('DELETE_ARTICLE', this.article.id)
        this.$router.push({name: 'index'})
    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  }
}
</script>

<style>

</style>
```

- index에는 v-for를 통해 article이 하나씩 나올 수 있도록 한다.

```js
<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{name:'create'}">게시글 작성</router-link>
    <ArticleItem
    v-for="(article, index) in articles"
    :key="index"
    :article=article
    />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'

export default {
  name: 'IndexView',
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>


# 하위 컴포넌트
<template>
  <div @click="goDetail(article.id)">
    <p>글 번호: {{ article.id }}</p>
    <p>제목{{ article.title }}</p>
    
  </div>
</template>

<script>
export default {
    name: 'ArticleItem',
    props: {
        article: Object,
    },
    methods: {
        goDetail(id) {
            this.$router.push({name:'detail', params: {id}})
        },
        
    }
}
</script>

<style>

</style>
```

- NotFound404는 간단히 제목만 작성하였다. route 경로를 잘 설정해주는 것이 중요!

```js
<template>
  <div>
    <h1>404 Not Found</h1>
  </div>
</template>

<script>
export default {
    name: 'NotFound404'
}
</script>

<style>

</style>
```

