# 06_django_practice

### 1. User Create

![image-20220911133752050](06_django_practice.assets/image-20220911133752050.png)

### 2. Login

![image-20220911133817425](06_django_practice.assets/image-20220911133817425.png)

![image-20220911133848380](06_django_practice.assets/image-20220911133848380.png)

### 3. Logout

![image-20220911133911057](06_django_practice.assets/image-20220911133911057.png)

### 4. User Update

![image-20220911133939870](06_django_practice.assets/image-20220911133939870.png)

### 5. User Delete

탈퇴완료

![image-20220911134015473](06_django_practice.assets/image-20220911134015473.png)

### Views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeFrom, CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_safe, require_POST

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.method == "POST":
        request.user.delete()
        auth_logout(request)
        return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeFrom(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeFrom(instance = request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)

@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm( request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/change_password.html', context)
```

### login.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>로그인</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
{% endblock content %}
```

### signup.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
{% endblock content %}
```

### update.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>회원정보 수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
{% endblock content %}
```

### urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name="update"),
    path('password/', views.change_password, name='change_password'),
]
```

### forms.py

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeFrom(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

