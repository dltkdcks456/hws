# Vuex

### 1.다음은Vuex 로 구성된 하나의 숫자를 counting 하는 store 이다
(a), (b), (c) 에 들어갈 코드를 작성하시오

- NUMBER_INCREMENT mutation handler 가 호출되면 state 의 count 를 1 만큼 증가시킨다.

```python
(a) - Vuex.Store
(b) - state.count += 1
(c) - context.commit('NUMBER_INCREMENT')
```



### 2.아래 예시의 함수는 서버로부터 데이터를 가져 온 뒤 , 응답 값을 state 에 저장하기 위하여 mutations 를 호출하는 로직을 수행한다
이와 같이 비동기 API 및 mutations 호출에 적합한 store 의 속성 ( a )를 작성하시오

```python
actions
```

### 3.
store에 정의한 state 를 직접 변경하지 않고 mutations 를 통해 변경해야 하는 이유를 Vuex 공식문서 를 참고하여 작성하시오

```python
state의 변화가 어떻게 진행되는지 데이터의 흐름과 그 코드를 빠르게 찾아낼 수 있다. 협업을 하거나 디버깅을 할 때에도 유용하고 효율적으로 사용할 수 있기 때문이다. 변경사항을 명시적으로 하기 위해서, 코드를 읽을 때 명확하게 추론하기 위해서이다.
```

