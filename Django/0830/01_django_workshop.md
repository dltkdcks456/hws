![image-20220901170149177](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220901170149177.png)

1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<str:food>/<int:member>/', views.dinner),
]
```

2. pages/views.py

```python
from django.shortcuts import render

# Create your views here.
def dinner(request, food, member):
    context={
        'food':food,
        'member': member,
    }
    return render(request, 'dinner.html', context)
```

3. templates/dinner.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>저녁메뉴추천</title>
</head>
<body>
    <h1>저녁 메뉴</h1>
    <h1>저녁 먹을 사람?!{{member}}명</h1>
    <h1>어떤 메뉴?! {{food}}</h1>
</body>
</html>
```

