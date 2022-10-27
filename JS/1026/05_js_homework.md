# JavaScript 심화

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다. 

```python
(T)
```

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다.

```python
(F): Web API에서 동작이 완료되면 Task queue로 가서 대기를 한 후에 Call Stack이 모두 완료되면 그 후에 할당된다.
```



### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

```python
동기: 요청한 일을 모두 수행할 때까지 다른 작업을 진행하지 못합니다.
비동기: 요청한 일의 작업 시간이 길어질 경우 기다리지 않고 다른 작업을 수행하는 것을 의미합니다. 미리 완료된 결과부터 보여주는 것을 일컫습니다.
```



### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오

```python
(a) - get
(b) - then
(c) - response.data
```

