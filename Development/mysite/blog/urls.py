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