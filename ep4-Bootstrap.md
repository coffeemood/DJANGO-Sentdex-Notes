# Bootstrap for HTML/CSS - Styling 

#### Bootstrap 

Bootstrap is a web-development framework made for HTML/CSS & Javascript. It provides us with the means to easily make an interactive, user-responsive webiste. 

After downloading Bootstrap and moving them into the `static` folder of the desired app, make sure we have a clause for **STATIC_URL** in `settings.py`

```
STATIC_URL = '/static/'
```

Next we want to reference the stylesheets into the header, we can do this easily using Jinja

```html
<--! header.html -->
<head>
{% load staticfiles %}
<link rel = "stylesheet" href = "{% static 'css/bootstrap.min.css'%}" type = "text/css"/>
</head>
```