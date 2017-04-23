from django.views.generic import View
from django.shortcuts import render,redirect
import matplotlib
import pandas as pd
from .models import Item, Discount, Statistic, Customer, Configuration
from .forms import ConfigurationForm
from django.conf import settings
from django.http import Http404
from . import AprioriClient
from django.conf import settings

def reset(request):
    stats_object = Statistic.objects.first()
    stats_object.rows_scanned = 1
    stats_object.run_time = 0.0
    stats_object.most_frequent_item = None
    stats_object.total_batches = 0
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
    f = open(settings.BASE_DIR+"/batchwise_local_frequent_one_item.csv", "w+")
    f.close()
    f = open(settings.BASE_DIR+"/batchwise_global_frequent_one_item.csv", "w+")
    f.close()
    return redirect('adminpanel:home')


def runAprioriClient(request):  
    AprioriClient.main()
    return redirect('adminpanel:home')


class AdminFormView(View):
    def get(self, request, *args, **kwargs):
        template = "AdminPanel/home.html"
        stats_object = Statistic.objects.first()
        item_count = Item.objects.count()
        customer_count = Customer.objects.count()
        discount_count = Discount.objects.count()
        discount_offers = Discount.objects.all()
        context = {
            'stats_object' : stats_object,
            'item_count' : item_count,
            'customer_count' : customer_count,
            'discount_count' : discount_count,
            'rows_scanned' : (stats_object.rows_scanned - 1),
            'discount_offers' : discount_offers,
        }
        return render(request, template, context)


class AssociationRules(View):

    def get(self, request, *args, **kwargs):
        try:
            association_rules = pd.read_csv(settings.BASE_DIR+"/association_rules.csv")
        except:
            raise Http404("No association rules generated")
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





class ConfigureSettings(View):
    def get(self, request, *args, **kwargs):
        conf_object = Configuration.objects.first()
        context = {
            'email_id':conf_object.admin_email_id,
            'email_password':conf_object.admin_email_password,
            'server_ip_address':conf_object.server_ip_address,
            'local_minimum_support':conf_object.local_minimum_support,
            'local_confidence':conf_object.local_confidence, 
        }
        conf_form = ConfigurationForm(context)
        template = "AdminPanel/configurations.html"
        return render(request, template,{'form':conf_form})

    def post(self, request, *args, **kwargs):
        conf_form = ConfigurationForm(request.POST)
        if conf_form.is_valid():
            conf_object = Configuration.objects.first()
            conf_object.admin_email_id = conf_form.cleaned_data['email_id']
            conf_object.admin_email_password = conf_form.cleaned_data['email_password']
            conf_object.server_ip_address = conf_form.cleaned_data['server_ip_address']
            conf_object.local_minimum_support = conf_form.cleaned_data['local_minimum_support']
            conf_object.local_confidence = conf_form.cleaned_data['local_confidence']
            conf_object.save()
            
        return redirect('adminpanel:home')