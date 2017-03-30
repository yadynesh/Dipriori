from django.contrib import admin
from .models import Customer,Item,Transaction,Discount,Statistic
from .forms import TransactionForm


class TransactionAdmin(admin.ModelAdmin):
    form = TransactionForm


class ItemAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item,ItemAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Discount)
admin.site.register(Statistic)

