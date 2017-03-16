from django.views.generic import View
from django.shortcuts import render

class AdminFormView(View):
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)
