# Django Model Relationship

### 1. M:N True or False

각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고, 틀렸다면 그 이유도 함께 작성하시오. 

1) Django에서 N:1 관계는 ForeignKeyField를 사용하고, M:N 관계는 ManyToManyField를 사용한다. 

```python
(T)
```

2. ManyToManyField를 설정하고 만들어지는 테이블 이름은 “앱이름_클래스이름_지정한 필드이름”의 형태로 만들어진다.  

```python
(F) 앱이름-클래스 이름-작성한 변수명
```



3) ManyToManyField의 첫번째 인자는 참조할 모델,  두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.

```python
(F): related_name은 선택적으로 활용이 가능하다. 추후 충돌이 발생하게 될 때에는 related_name을 작성해주어 버그를 해결한다.
```



### 2. Like in templates

아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

```python
(a): request.user
(b): article.like_users.all
```



### 3. Follow in views

```python
(a): user_pk
(b): followers
(c): filter
(d): remove
(e): add
```



### 4. User AttributeError

다음과 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오. 

```python
User 모델을 커스텀으로 변경해주지 않아서 에러가 발생했습니다.
# accounts/models.py
class User(AbstractUser):
    pass
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```



### 5. related_name

아래의 경우 ForeignKey 혹은 ManyToManyField에 related_name을 필수적으로 작성해야 한다. 그 이유를 설명하시오.

```python
user가 작성한 글들(user.article_set)
user가 좋아요를 누른 글(user.article_set)을 구분할 수 없어 충돌이 일어나기 때문에 둘 중 하나는 related_name으로 바꿔주어야 한다.
```



### 6. follow templates

```python
(a): person.followings.all
(b): person.followers.all
(c): request.user
(d): person
(e): person.pk
```

