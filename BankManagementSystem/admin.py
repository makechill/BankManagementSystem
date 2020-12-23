from django.contrib import admin
from .models import Banks, CreateAccount, Transactions

admin.site.register(Banks)
admin.site.register(CreateAccount) 
admin.site.register(Transactions) 
# Register your models here.

