# Vue 기초

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- SPA는 Single Pattern Application의 약자이다. 

```python
(F) - Single Page Application
```

- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고,  이후부터는 페이지 갱신에 필요한 데이터만 전달받는다. 

```python
(T)
```

- Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트되는 것을 의미한다. 

```python
(T) 사용자의 응답에 따라 변하는 것을 의미한다.
```

- v-bind 디렉티브는 “@“, v-on 디렉티브는 “:” shortcut(약어)을 제공한다. 

```python
v-on은  @ , v-bind는 : 의 약어를 사용한다.
```

-  v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다

```python
v-model은 양방향 바인딩이다.
```



### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오

```python
View - 우리 눈에 보이는 부분 = DOM
Model - 실제 데이터 = JSON!
View Model(Vue)
- View를 위한 모델
- View와 연결되어 Action을 주고 받음
- Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
- View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 view도 변경됨
```



### 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

```python
(a) - message
(b) - new Vue
(c) - '#app'
```

