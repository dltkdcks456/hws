# Django Model Relationship



![](C:\Users\SSAFY_SangChan\AppData\Roaming\Typora\typora-user-images\image-20221012232514520.png)

```python
# views.py
def likes(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    if restaurant.like_users.filter(pk=request.user.pk).exists():
        restaurant.like_users.remove(request.user)
    else:
        restaurant.like_users.add(request.user)
    return redirect('restaurants:index')



# models.py
from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_restaurants')
    region = models.CharField(max_length=1000)
    name = models.CharField(max_length = 200)
    stars = models.IntegerField()
    bestMenu = models.CharField(max_length=200)
    reason = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, upload_to = 'images/%Y/%m/%d')
    
    def __str__(self):
        return self.name
    
    
    
    
# index.html
{% extends 'base.html' %}
{% load static %}

{% block content %}
    {% comment %} <img src="{% static 'restaurants/16095.jpg' %}" alt="" style="width:500px"> {% endcomment %}
    <img src="{% static 'food.gif' %}" alt="" style="width:600px">
    <h1 class="m-3"> 부울경 2반 맛집 </h1>
    {% if  restaurants %}
    <ul class="list-group ">
        {% for restaurant  in restaurants  %}
            <li class=" list-group-item "> 
                <a href="{% url 'restaurants:detail' restaurant.pk %} " class="fw-bold btn btn-success text-decoration-none text-white">{{ restaurant.name }}</a> 
                <div class="mt-2">
                    <form action="{% url 'restaurants:like' restaurant.pk %}" method="POST">
                        {% csrf_token %}
                        {% if request.user in restaurant.like_users.all %}
                          <input type="submit" value="좋아요 취소" class="btn btn-warning fw-bold">
                        {% else %}
                          <input type="submit" value="좋아요" class="btn btn-warning fw-bold">
                        {% endif %}
                    </form>
                </div>
                <p class="mt-3">{{ restaurant.like_users.all|length }}명이 좋아합니다.</p>
            </li>
        {% endfor %}
    </ul>
    {% endif %}

    <a href="{% url 'restaurants:create' %}" class="btn btn-info text-white mt-4">맛집 추천하기</a>
{% endblock content %}
```

