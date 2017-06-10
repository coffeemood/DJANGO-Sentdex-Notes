from django.shortcuts import render
# Create your views here.

def index(request):
	return render(request, 'mypersonalpage/home.html')


def contact(request):
	return render(request, 'mypersonalpage/basic.html', {'content': ['Please email the headmaster by referring to his local pub overlord', 'figuituot@gmail.com']})
