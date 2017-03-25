from django.views.generic import View
from django.shortcuts import render
import matplotlib



class AdminFormView(View):
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)

def runAprioriClient(request):
    from . import AprioriClient
    template = "AdminPanel/home.html"
    return render(request, template,)