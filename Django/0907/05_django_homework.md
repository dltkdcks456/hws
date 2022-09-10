# Django Authentication System

### 1. Django User Model 

Django에서 기본적으로 사용하는 User 모델은 아래의 경로에서 찾아볼 수 있다. Django 공식 github에서 User 모델이 정의된 코드를 찾아본 후 우리가 User 모델을 대체 시 AbstractUser를 상속 받는 부모 클래스로 설정한 이유를 작성해보시오

![image-20220907225421527](05_django_homework.assets/image-20220907225421527.png)

```python
대부분의 기능이 AbstractUser 클래스에서 구현되므로 User모델을 대체 시 해당 클래스를 상속 받는 부모 클래스로 설정한다.
```

### 2. Create user by ModelForm

새 유저를 생성하기 위해서 Django 내부에 정의된 ModelForm을 사용하려 한다. 이 때 유저 생성 form을 사용하기 위해 작성하는 import 구문을 적으시오.

```python
from django.contrib.auth.forms import UserCreationForm
```

### 3. Django sessions

Django는 사용자가 로그인에 성공할 경우 (a) 테이블에 세션 데이터를 저장한다. 그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 (b)다. (a)와 (b)에 알맞은 값을 작성하시오

```python
(a): django_session
(b): session_id
```

