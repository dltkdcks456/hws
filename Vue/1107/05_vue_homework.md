# 05_vue_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다.

```python
(F) props & emit 방식으로도 상태관리를 할 수 있다.
```

mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다.

```python
(T)
```

mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다.

```python
(F) mutations 는 $store.commit 으로 actions 는 $store.dispatch 로 호출할 수 있다.
```

state는 data의 역할, getters는 computed와 유사한 역할을 담당한다.

```python
(T)
```

### 2. Vuex에서 State, Getters, Mutations, Actions의 역할을 각각 서술하시오

```python
- State: vue 인스턴스의 data에 해당. 중앙에서 관리하는 모든 data
- Getters: vue 인스턴스의 computed에 해당. state를 활용하여 계산된 값을 얻고자 할 때 사용
- Mutations: state를 변경하고자 할 때 사용
- Actions: mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있다. state를 직접 변경하지 않고 `commit()` 메서드로 mutations를 호출해서 state를 변경
```

### 3. 컴포넌트에 작성된 Todo App 관련 코드를 Vuex의 Store로 옮기고자 한다.  빈 칸 (a), (b), (c), (d)에 들어갈 코드를 작성하시오.

```python
(a) state
(b) getters
(c) mutations
(d) state
```

### 4.Vue Life Cycle Hook 을 참고하여 , 다음 Vue application 을 실행했을 때 console 창에 출력되는 메시지를 작성하시오

```python
created!
mounted!
```

