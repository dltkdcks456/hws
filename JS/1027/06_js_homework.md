# JavaScript 심화

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다. 

```python
(T)
```

- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다.  XHR객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다. 

```python
(T)
```

- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.

```python
(T)
```

### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```python
1. console.log('Hello SSAFY!')가 Call Stack으로 들어간 후 출력됨 -> Hello SSAFY!
2. setTimeout(function () {console.log('I am from setTimeout')}, 1000) 이 Call Stack으로 들어감
3. setTimeout 은 바로 수행이 되지 않으므로 Web API로 넘어가서 수행됨
4. 기다리는 동안 console.log('Bye SSAFY!')가 Call Stack으로 들어간 후 출력됨 -> Bye SSAFY!
5. Web API에서 처리된 setTimeout 안의 함수가 Task Queue로 넘어감
6. Event Loop가 Call Stack이 빈 것을 확인하면 Task Queue 내에 가장 오래된 함수 function()를 Call Stack으로 이동시킴
7. function()이 실행되고 console.log('I am from setTimeout')이  Call Stack으로 들어온 후 출력됨 -> I am from setTimeout
```

