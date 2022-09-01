![image-20220901172044229](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220901172044229.png)

1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```

2. pages/views.py

```python
from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    a = list(range(1, 46))
    lotto = random.sample(a, 6)
    context = {
        'lotto': lotto
    }
    return render(request, 'lotto.html', context)
```

3. templates/lotto.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>로또 추천 머신</title>
</head>
<body>
    <h1>제 OOO회 로또 번호 추천</h1>
    <p>SSAFY님께서 선택하신 로또 번호는 {{lotto}}입니다.</p>
</body>
</html>
```

