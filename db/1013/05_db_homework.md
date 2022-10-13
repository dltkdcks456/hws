# Django Model Relationship

### 1. MTV

Django는 MTV로 이루어진 Web Framework다.  MTV가 무엇의 약자이며 Django에서 각각 어떤 역할을 하고 있는지 작성하시오.

```python
M: Model -> 데이터를 가지고 있으며, 데이터를 처리하는 로직
T: Template -> 화면에 요청에 대한 결과물을 보여주는 역할
V: View -> 모델과 뷰를 이어주는 역할, 요청에 따라 적절한 로직을 가동하도록 알려주고 모델이 응답하면 그 응답을 뷰에 전달하는 역할
```



### 2. 404 Page not found 

기본적으로 ‘/ ’ 페이지에 접속하게 되면 아래 사진처럼 Page not found 에러가 발생한다.  ‘/ ’ 페이지에 접속했을 때 index.html를 렌더링 하고자 한다. 아래 빈칸에 알맞은 코드를 작성하시오. (프로젝트의 이름은 crud 이며 app 이름은 articles이다. index.html 파일을 렌더링 하는 view 함수의 이름은 index라고 가정한다.)

```python
(a): articles
(b): views
(c): views.index
```



### 3. templates and static

Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static 파일을 앱 폴더 내부의 templates와 static 이름의 폴더에서 찾는다.  만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 __(a)__ 파일의 __(b)__와 __(c)__ 라는 변수에 담긴 리스트의 요소를 정의하면 된다.  빈칸 (a), (b), (c)에 들어갈 내용을 작성하시오. 

```python
(a): settings.py
(b): STATICFILES_DIRS
(c): [BASE_DIR / 'static']
```



### 4. migration

```python
(1) python manage.py makemigrations
(2) python manage.py showmigrations
(3) python manage.py sqlmigrate articles 0001
(4) python manage.py migrate
```



### 5. ModelForm True or False

각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.  

1) POST와 GET 방식은 의미론상의 차이이며 실제 동작 방식은 동일하다. 
2) ModelForm과 Form Class의 핵심 차이는 Model의 정보를 알고 있는지의 여부이다. 
3) AuthenticationForm은 User 모델과 관련된 정보를 이미 알고 있는 ModelForm으로 구성되어 있다. 

4) ModelForm을 사용할 때 Meta 클래스에 fields 관련 옵션은 반드시 작성해야 한다.

```python
1. (F): GET은 주로 조회에 사용하며 POST는 삽입, 생성, 수정에 이용하면 csrf token과 같은 보안과 관련된 역할도 추가된다.
2. (T): ModelForm은 Meta클래스를 활용해 모델의 정보를 알고 있지만, Form은 하나씩 맵핑을 해주어야한다.
3. (F): 로그인관련 페이지를 보여주는 Form으로 구성되어 있다.
4. (F): fields를 작성하지 않으면 전부를 출력해준다.
```



### 6. media 파일 경로

사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더(crud) 내부의 /uploaded_files 폴더로 지정하고자 한다.  이 때, settings.py에 작성해야 하는 설정 2가지를 작성하시오.

```python
1. MEDIA_ROOT = BASE_DIR / 'media'
2. MEDIA_URL = '/media/'
```



### 7. DB True or False

각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오. 

1) RDBMS를 조작하기 위해서 SQL문을 사용한다. 

2) SQL에서 명령어는 반드시 대문자로 작성해야 동작한다.  

3) 일반적인 SQL문에서는 세미콜론( ; )까지를 하나의 명령어로 간주한다. 

4) SQLite에서 .tables, .headers on과 같은 dot( . )로 시작하는 명령어는 SQL문이 아니다.  

5) 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다.

```python
(1): T -> SQL문으로 RDBMS를 조작한다
(2): F -> 소문자로도 작성되지만 가독성이 떨어지므로 관례상 대문자로 작성한다
(3): T -> 세미콜론이 주어져야 명령이 실행된다
(4): F -> .tables는 테이블의 목록을 표시해준다.
(5): F -> 하나의 데이터베이스 안에는 여러 테이블을 만들 수 있다.
```



### 8. on_delete

게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 즉, ProtectedError를 발생시켜 참조 된 객체의 삭제를 방지하는 __(a)__를 작성하시오.

```python
(a): PROTECT
```



### 9. Like in models Article

Article 모델과 User 모델을 M:N 관계로 설정하여 ‘좋아요’ 기능을 구현하려고 한다. __(a)__와 __(b)__에 들어갈 내용을 작성하시오. 

```python
(a): ManyToManyField
(b): related_name
```



### 10. Follow in models

follow 기능을 구현하기 위해 accounts app의 models.py에 아래와 같은 모델을 작성하였다. Migration 작업 이후에 Database에 만들어지는 중개 테이블의 이름을 작성 하고 이 테이블의 id를 제외한 컬럼 이름을 각각 작성하시오.

```python
accounts_user_followings
from_user_id
to_user_id
```

