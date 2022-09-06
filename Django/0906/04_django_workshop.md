# 04_django_workshop

Django Model Form을 활용해 CRUD을 모두 갖춘 장고 프로젝트를 제작하고 결과 사진과 코드(url, view, template, model)를 별도의 마크다운 파일에 작성하여 제출 하시오.

### INDEX page

![image-20220907083959073](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20220907083959073.png)

### CREATE page

![image-20220907084037848](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20220907084037848.png)

### UPDATE page

![image-20220907084104926](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20220907084104926.png)

### DETAIL page

![image-20220907084119919](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20220907084119919.png)

### articles app폴더 내

- creat.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>CREATE</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        {% comment %} <label for="title">Title:</label>
        <input type="text" id='title' name='title'>
        <label for="content">Content:</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea> {% endcomment %}
        <input type="submit" value='CREATE'>
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```

- detail.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Detail</h1>
    <hr>
    <h1>글 번호: {{article.pk}}</h1>
    <h1>글 제목: {{article.title}}</h1>
    <p>글 내용: {{article.content}}</p>
    <p>글 생성시각: {{article.created_at}}</p>
    <p>글 수정시각: {{article.updated_at}}</p>
    <hr>
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
    <a href="{% url 'articles:index' %}">BACK</a><br>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
    </form>
{% endblock content %}
```

- index.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Articles</h1>
    <a href="{% url 'articles:create' %}">CREATE</a>
    <hr>
    {% for article in articles %}
      <h1>Title : {{article.title}}</h1>
      <a href="{% url 'articles:detail' article.pk%}">DETAIL</a>
      <hr>
    {% endfor %}
{% endblock content %}
```

- update.html

```html
{% extends 'base.html' %}

{% block content %}
    <h1>UPDATE</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="UPDATE">
    </form>
    <hr>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock content %}
```

- forms.py

```python
from turtle import textinput
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
                'max-length' : 10,
            }
        )
    
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages={
            'required':'Please enter your content'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'
```

- models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
]
```

- views.py

```python
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
            'form':form,
    }
    return render(request, 'articles/create.html', context)
        

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['POST', 'GET'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form':form
    }
    return render(request, 'articles/update.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

### crud 폴더 내

- settings.py

```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

### templates 내부

- base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <title>04_django_workshop</title>
</head>
<body class='container'>
    {% block content %}
    {% endblock content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

