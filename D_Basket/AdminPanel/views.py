from django.views.generic import View
from django.shortcuts import render
import matplotlib

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse
import pandas as pd
import seaborn


class AdminFormView(View):
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)

def graph(request, itemset):
    fig = Figure()
    
    fig.set_size_inches(15, 6, forward=True)

    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.35)
    

    final_itemset = pd.Series()
    print("itemset="+str(itemset))
    
    if int(itemset) == 1:
    	final_itemset = pd.Series.from_csv("C:/Users/yadynesh/Final_Project/D_Basket/final_one_itemset.csv")

    	print(final_itemset)
    	final_itemset.T.plot.bar(ax=ax)

    if int(itemset) == 2:
    	final_itemset = pd.Series.from_csv("C:/Users/yadynesh/Final_Project/D_Basket/final_two_itemset.csv")
    	final_itemset= final_itemset[final_itemset>50000]
    	final_itemset.plot.bar(ax=ax)

    if int(itemset) == 3:
    	final_itemset = pd.Series.from_csv("C:/Users/yadynesh/Final_Project/D_Basket/final_three_itemset.csv")
    	final_itemset= final_itemset[final_itemset>40000]
    	final_itemset.plot.bar(ax=ax)

    canvas = FigureCanvas(fig)
    response = HttpResponse( content_type = 'image/png')
    canvas.print_png(response)
    return response