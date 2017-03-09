from django.shortcuts import render

# Create your views here.

def loadHome(request):
	template_name = 'AdminPanel/home.html'
	return render(request,template_name,)
