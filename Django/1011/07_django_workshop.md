# Static/Media

### 1. 스크린 샷과 달리 index 페이지에서메인 이미지가 출력되지않는다.  이를 해결하시오.

```python
# static_media/urls.py에 하기 코드를 추가해준다. 추가 경로에도 이미지를 불러올 수 있도록 한다.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```



### 2. 이미지를 첨부하여게시글을 작성해보자. 게시글은 작성되는듯 하지만 “업로드된 이미지가 없습니다!” 라는 문구가 출력된다. 올바르게 이미지가업로드 되어 index 페이지 각 게시글에 출력 될 수 있도록 이를 해결하시오.

```python
# static_media/settings.py에 media url과 파일 경로를 불러올 수 있게 코드를 작성
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# articles/templtes/articles/create.html
# enctype으로 바이너리 데이터를 읽을 수 있게 바꿔준다.
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>CREATE</h1>
  <form action="" method="POST" enctype='multipart/form-data'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
</body>
</html>
```

