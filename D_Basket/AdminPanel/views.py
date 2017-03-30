from django.views.generic import View
from django.shortcuts import render,redirect
import matplotlib
import pandas as pd
from .models import Item, Discount, Statistic
from django.conf import settings

def reset(request):
    stats_object = Statistic.objects.first()
    stats_object.rows_scanned = 1
    stats_object.save()
    f = open(settings.BASE_DIR+"/association_rules.csv", "w+")
    f.close()
    f = open(settings.BASE_DIR+"/final_one_itemset.csv", "w+")
    f.close()
    f = open(settings.BASE_DIR+"/final_two_itemset.csv", "w+")
    f.close()
    f = open(settings.BASE_DIR+"/final_three_itemset.csv", "w+")
    f.close()
    f = open(settings.BASE_DIR+"/batchwise_one_item_count.csv", "w+")
    f.close()
    template = "AdminPanel/home.html"
    return render(request, template)


def runAprioriClient(request):
    from . import AprioriClient
    return redirect('adminpanel:home')


class AdminFormView(View):
    def get(self, request, *args, **kwargs):
        template = "AdminPanel/home.html"
        stats_object = Statistic.objects.first()
        context = {
            'stats_object' : stats_object
        }
        return render(request, template, context)


class AssociationRules(View):

    def get(self, request, *args, **kwargs):
        association_rules = pd.read_csv(settings.BASE_DIR+"/association_rules.csv")
        print(association_rules)
        template = "AdminPanel/association_rules.html"
        return render(request, template,{'association_rules':association_rules})


    def post(self, request, *args, **kwargs):
        print(request.POST['ass_left'])

        left_items = request.POST['ass_left'].split(",")  
        left_item1 = Item.objects.get(item_name = left_items[0])
        left_item2 = None
        if(len(left_items) == 2):
            left_item2 = Item.objects.get(item_name = left_items[1])

        right_items = request.POST['ass_right'].split(",")  
        right_item1 = Item.objects.get(item_name = right_items[0])
        right_item2 = None
        if(len(right_items) == 2):
            right_item2 = Item.objects.get(item_name = right_items[1])

        discount = request.POST['discount']

        discount = Discount(left_item1 = left_item1,left_item2 = left_item2,right_item1 = right_item1,right_item2 = right_item2,discount_percent = discount)
        discount.save()

        return redirect('adminpanel:list-discounts')



