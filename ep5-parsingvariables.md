# Parsing Variables using Jinja 

#### Creating a basic page to return contact information 

```python 
#views.py 

def contact(request):
    return render(request, 'mypersonalpage/basic.html', {'content': ['Please email the headmaster by referring to his local pub overlord', 'figuituot@gmail.com']})

```


We then need to create a `basic.html` template which parse the dictionary values above to the page

```html
{% extends "mypersonalpage/header.html" %}

{% block content %}

    {% for c in content %}
        <p>{{c}}</p>
    {% endfor %}

{% endblock %}
```

Then we simple pass this into `urls.py`

```python
from django.conf.urls import url, include 
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/', views.contact, name = 'contact')
]
```

[!] Note that this allows us to refer to an URL that is **not the same** as the exact path on the server. It's one of the advantages of this framework compared to traditional web development