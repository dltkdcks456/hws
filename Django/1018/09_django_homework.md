# Django REST Framework

### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. 

```python
(T): REST API의 기본 원칙이다.
```

HTTP Method는 GET과 POST 두 종류 뿐이다. 

```python
(F) HTTP Method는 다양한 종류가 있으며 GET, POST 뿐만 아니라 PUT, DELETE 등등이 존재한다.
https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
```

‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.

```python
(F) path를 나타낼 때 조금더 간략하게 표현하면 더 잘 
```



### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

200(OK)  - 요청이 성공했음을 나타내는 성공 응답 상태 코드입니다.

400(Bad Request) - 서버가 클라이언트 오류(예: 잘못된 요청 구문, 유요하지 않은 요청 메시지 프레이밍) 를 감지해 요청을 처리할 수 없거나, 하지 않는다는 것을 의미. 잘못된 문법, 서버에서 요청을 이해할 수 없습니다.

401(Unauthorized) - 해당 리소스에 유효한 인증 자격 증명이 없기 때문에 요청이 적용되지 않았음을 나타냅니다.

403(Forbidden) - 서버에 요청이 전달되었지만, 콘텐츠에 접근할 권한 때문에 거절되었다는 것을 의미입니다. (틀린 비밀번호로 로그인 하는 경우)

404(Not Found) - 서버가 요청받은 리소스를 찾을 수 없다는 것을 의미, URL을 찾을 수 없습니다.

500(Internal Server Error) - 요청을 처리하는 과정에서 서버가 예상하지 못한 상황에 놓였다는 것을 나타냅니다.

### 3. 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

```python
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
```

### 4. Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오

```python
DB에 있는 테이블을 HTML, JSON 등등으로 쉽게 변환할 수 있도록 도와주는 기능이며, 다양한 메소드를 제공해주어 쉽게 개발을 할 수 있다.
```

