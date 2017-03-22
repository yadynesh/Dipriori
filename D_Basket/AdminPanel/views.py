from django.views.generic import View
from django.shortcuts import render
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.http import HttpResponse
import pandas as pd


class AdminFormView(View):
	def get(self, request, *args, **kwargs):
		template = "AdminPanel/home.html"
		return render(request, template,)


# def graph(request):
#     fig = Figure()
#     #ax = fig.add_subplot(111)
#     data_df = pd.read_csv("C:/Users/yadynesh/Final_Project/original1.csv")
#     data_df = pd.DataFrame(data_df)
#     one_item_count = data_df.sum(axis=0)
#     print("One Item Count:\n\n"+str(one_item_count))
#    	#one_item_count.plot()
#     frequent_one_item_count = one_item_count[one_item_count >= 1000]
#     frequent_one_item_count.plot()
#     #plt.show()
#     canvas = FigureCanvas(fig)
#     response = HttpResponse( content_type = 'image/png')
#     canvas.print_png(response)
#     return response

def graph(request):
    fig = Figure()
    #ax = fig.add_subplot(111)
    data_df = pd.read_csv("C:/Users/yadynesh/Final_Project/original1.csv")
    data_df = pd.DataFrame(data_df)
    
    one_item_count = data_df.sum(axis=0)
    data_df.plot()
    print(type(one_item_count))
    canvas = FigureCanvas(fig)
    response = HttpResponse( content_type = 'image/png')
    canvas.print_png(response)
    return response