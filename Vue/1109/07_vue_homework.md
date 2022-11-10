# Vue Router

### 1.아래의 설명을 읽고 T/F 여부를 작성하시오
UX와 UI 는 동일한 의미로 많이 사용한다

```python
(F): UX는 사용자의 경험을 토대로 디자인 구성
	 UI는 유저에게 보여지는 화면을 디자인
```

UX는 직감으로 결정되는 것이 아니라 하나의 학문으로 연구되는 중요한 분야이다

```python
(T): 심리학에서도 연구되는 중이다.
```

URL라우팅은 Server 에서만 할 수 있으며 SPA 로 개발하는 Front 에서는 필요없다

```python
(F): URL routing은 SPA를 MPA처럼 활용할 수 있도록 Front에서 사용한다.
```

Django의 variable routing 처럼 주소로 전달된 값을 사용할 수 있다

```python
(T): variable routing처럼 활용하여 컴포넌트의 내용을 구성할 수 있다.
```



### 2. Vue Router에서 설정하는 history mode 가 무엇을 뜻하는지 서술하시오

```python
브라우저의 History API를 활용한 방식, 새로고침 없이 URL 이동 기록을 남길 수 있고 뒤로가기 기능을 가능하게 해준다.
```



### 3. 다음 localhost:8080/about 경로를 통하여 views AboutView vue 컴포넌트를 보여주기 위한 코드이다 . 코드의 빈 칸 (a), (b), (c) 를 채우시오
```python
(a)- import AboutView from '@/views/AboutView.vue'
(b)- '/about'
(c)- component
```

