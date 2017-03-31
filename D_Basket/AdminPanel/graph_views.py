from django.conf import settings
from django.views.generic import View
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
import seaborn


def graph_main(request,type):
    return render(request,'AdminPanel/graphs.html',{'type':type})


def barChart(request, itemset):
    fig = Figure()
    fig.set_size_inches(15, 6, forward=True)

    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.35)
    

    final_itemset = pd.Series()
    #print("itemset="+str(itemset))
    
    if int(itemset) == 1:
        final_itemset = pd.Series.from_csv(settings.BASE_DIR+"/final_one_itemset.csv")
        final_itemset.T.plot.bar(ax=ax)

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

    final_itemset.iloc[int(batch_number)-1].plot.bar(ax=ax)


    canvas = FigureCanvas(fig)
    response = HttpResponse( content_type = 'image/png')
    canvas.print_png(response)
    return response

