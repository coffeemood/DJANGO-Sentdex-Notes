# Building a Blog App

In this tutorial we will be building a separate blog app. 

#### Django Models

In models.py, every class is similar to a table, and each variable is a column

Sample Model: 

```python 
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self): 
        return self.title #This is to reference the string of title so it won't return the whole post object
```

#### Generic Display Views 

This time we will create our views using ListView (a type of Generic View): 

```python 
#urls.py

from django.conf.urls import url, include 
from django.views.generic import ListView, DetailView 
from blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Post.object.all().order_by("-date"),
        template_name = "blog/blog.html"))
    # This use ListView to return a list of objects as view. We query the db for 
    # dates then list it all out. We can also specify a limit if there are way too many 
    # posts using [:x]

]
```

#### Template calling `object_list` 

We then need to create a simple template for the blog

```html
{% extends "mypersonalpage/header.html" %}

{% block content %}
{% for post in object_list %}
    <h5>{{ post.date |date:"Y-m-d"}}<a href="/blog/{{post.id}}"> {{post.title}}</a></h5>
{% endfor %}
{% endblock %}
```

