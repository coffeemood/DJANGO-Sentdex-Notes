# Individual Blog Pages

#### Adding `urls.py`

For this one we need to add a special url pattern into urls.py to parse all individual blog posts using primary key and also sanitse input through regex

```python 
from django.conf.urls import url, include 
from django.views.generic import ListView, DetailView 
from blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date"),
        template_name = "blog/blog.html")),
    # This use ListView to return a list of objects as view. We query the db for 
    # dates then list it all out. We can also specify a limit if there are way too many 
    # posts using [:x]
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name = "blog/post.html" ))

]
```

#### Making the `post.html` template

```html
{% extends "mypersonalpage/header.html" %}

{% block content %}

<h3> {{ post.title }} </h3>
<br>
<hr>
<h6> Publish Date: {{ post.date }} </h6>
{{ post.body|safe|linebreaks}}

{% endblock %}
```

There are a couple of things **to note** from the above code: 

|--|--|
|`safe` | allows us to freely edit our notes with html style tags |and still be able to parse it onto the screen without problems |
|`linebreaks` | is what it sounds like, it adds a line break every time there is a break in the post | 


