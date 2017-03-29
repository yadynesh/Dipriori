from django.views.generic import View
from django.shortcuts import render
import matplotlib
import pandas as pd
from django.conf import settings


class AdminFormView(View):
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)

def runAprioriClient(request):
    from . import AprioriClient
    template = "AdminPanel/home.html"
    return render(request, template,)

def getAssociationRules(request):
    association_rules = pd.read_csv(settings.BASE_DIR+"/association_rules.csv")
    print(association_rules)
    template = "AdminPanel/association_rules.html"
    return render(request, template,{'association_rules':association_rules})