from django.conf import settings
from django.views.generic import View
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
import seaborn
from .models import Statistic
from .graph_forms import BatchStatisticsForm,BatchCompareForm


#This method loads the main graph page.It takes the type of graph as a parameter.Current the only type is "bar".
def graph_main(request,type):
    return render(request,'AdminPanel/graphs.html',{'type':type})


#This method generates bar chart of one,two or three itemset in imageview.
def barChart(request, itemset):
    fig = Figure()
    fig.set_size_inches(15, 6, forward=True)

    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.35)
    

    final_itemset = pd.Series()
    
    if int(itemset) == 1:
        final_itemset = pd.Series.from_csv(settings.BASE_DIR+"/final_one_itemset.csv")
        final_itemset.T.plot.bar(ax=ax)
        #T stands for transpose.It is used because final_itemset is a series.

    if int(itemset) == 2:
        final_itemset = pd.Series.from_csv(settings.BASE_DIR+"/final_two_itemset.csv")
        final_itemset= final_itemset[final_itemset>50000]
        final_itemset.plot.bar(ax=ax)

    if int(itemset) == 3:
        final_itemset = pd.Series.from_csv(settings.BASE_DIR+"/final_three_itemset.csv")
        final_itemset= final_itemset[final_itemset>40000]
        final_itemset.plot.bar(ax=ax)

    canvas = FigureCanvas(fig)
    response = HttpResponse( content_type = 'image/png')
    canvas.print_png(response)
    return response

#This class is used to generate barcharts or statitics batchwise.
class BatchStatistics(View):
    def get(self, request, *args, **kwargs):
        batch_form = BatchStatisticsForm()
        return render(request,'AdminPanel/batchwise_statistics.html',{'batch_form' : batch_form})

    def post(self, request, *args, **kwargs):
        batch_form = BatchStatisticsForm(request.POST)
        if batch_form.is_valid():
            batch_number =  batch_form.cleaned_data['batch_number']
            return render(request,'AdminPanel/batchwise_statistics.html',{'batch_form' : batch_form, 'batch_number': batch_number})


#This class is used to compare two batches.
class BatchCompare(View):
    def get(self, request, *args, **kwargs):
        batch_compare_form = BatchCompareForm()
        return render(request,'AdminPanel/compare_local_batch.html',{'batch_compare_form' : batch_compare_form})

    def post(self, request, *args, **kwargs):
        batch_compare_form = BatchCompareForm(request.POST)
        if batch_compare_form.is_valid():
            batch_number_1 =  batch_compare_form.cleaned_data['batch_number_1']
            batch_number_2 =  batch_compare_form.cleaned_data['batch_number_2']
            context = {
                'batch_compare_form' : batch_compare_form,
                'batch_number1': batch_number_1,
                'batch_number2': batch_number_2 

            }
            return render(request,'AdminPanel/compare_local_batch.html',context)

#This method is used to generate barchart for a particular batch.
def batchwise_barchart(request, itemset_type, batch_number):
    fig = Figure()
    fig.set_size_inches(15, 6, forward=True)

    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.35)
    
    if itemset_type == "local":
        final_itemset = pd.read_csv(settings.BASE_DIR + "/batchwise_one_item_count.csv")
    elif itemset_type == "localfrequent":
        final_itemset = pd.read_csv(settings.BASE_DIR + "/batchwise_local_frequent_one_item.csv")
    elif itemset_type == "globalfrequent":
        final_itemset = pd.read_csv(settings.BASE_DIR + "/batchwise_global_frequent_one_item.csv")
    print(final_itemset)

    print("bacthwise")
    final_itemset = final_itemset.iloc[int(batch_number)-1]
    print(final_itemset)
    final_itemset.plot.bar(ax=ax)
    print("catch")

    canvas = FigureCanvas(fig)
    response = HttpResponse( content_type = 'image/png')
    canvas.print_png(response)
    return response
