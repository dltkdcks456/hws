# Vue Router

### 1.아래의 설명을 읽고 T/F 여부를 작성하시오
동적으로 인자를 주소로 전달했을 때 해당 변수에 접근하는 방법은 router. params를 이용해서 접근할 수 있다
```python
(F): $route.params를 활용한다.
```

전체route 가 아닌 특정 route 에 대해서만 가드를 설정하고 싶을 때 beforRouteUpdate () 를 사용한다
```python
(F): 라우터 가드인 경우 beforeEnter()를 사용한다.
```

라우터 가드의 콜백 함수의 인자는 to, from, next 에 대한 값을 인자로 받는다
```python
(T): to는 이동할 URL 정보가 담긴 Route 객체
from: 현재 URL 정보가 담긴 Route 객체
next: 지정한 URL로 이동하기 위해 호출하는 함수
```

사용자가 요청한 리소스가 존재하지 않을 때 404 NOT FOUND 페이지를 표시할 수 있다

```python
(T): route를 활용해서 리소스가 없거나 그 외의 URL에 접속했을 때 404 NOT FOUND로 페이지를 표시하게 할 수 있다.
```

### 2. lazy loading 를 사용하는 이유를 다음 공식 문서 에서 확인하여 작성하시오
```python
한번에 모든 component를 불러오게 되면, 그 시간이 길어져서 사용자가 불편함을 느낄 수 있기 때문에 컴포넌트 별로 분할해서 클릭이 되었을 때 실행이 되도록 lazy loading을 사용한다.
```

### 3.다음은 요청하는 경로가 없을 때 Not Found 404 페이지를 보여주기 위한 코드이다 . 코드의 빈 칸을 작성하시오
```python
(a) - '*'
(b) - redirect
```

