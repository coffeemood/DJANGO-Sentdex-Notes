# Creating our first app - Personal Website 

After initialising our project, we want to create an app

```
python ./manage.py startapp webapp
```

#### Tests 

The concept of test is that we can fill out a script and the tests will run automatically every time we want to check if the system is functioning correctly, that way we don't have to do it manually

#### Jinja Templating Language 

Writing dynamic/logical HTML which helps creating consistent content page to page.

[!] When creating templates, we want to store another sub directory of the same name as the app in side templates. This is because django collect all templates of all apps and render them together so duplicates would cause complications 

**E.g: /mypersonalpage/templates/mypersonalpage/*.html**


##### Using `extend` to logically display page 

When we are creating a template to **extend**, we can then simply include a logic clause and Django will know to extend that file no matter what app is running the code 

```html
{% extends "mypersonalpage/header.html" %}
```

```html
#header.html 

<!DOCTYPE HTML>
<html lang = 'en'>
<head>
    <title> Nam's Lost Notebook </title>
    <meta charset = 'utf-8' />
</head>
<body>
    <div>
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>

```

```html 
#home.html
{% extends "mypersonalpage/header.html" %}

{% block content %}

<p> Hello, Welcome to the hunt for Nams' lost treasures. I hope you're ready! </p>

{% endblock %}
```

##### `includes`

We often use `extends` to render stuffs that need to stay consistent all the time like headers & footers. With `includes` we can be more flexible and add whatever we want anywhere we want so it can involve other contents as well.

`{% includes mypersonalpage/includes/snippet.html%}`
