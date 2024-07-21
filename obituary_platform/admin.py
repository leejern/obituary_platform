from django.contrib import admin

# Register your models here.
from . models import * 

class ObituaryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'date_of_birth', 'date_of_death', 'author', 'submission_date')
    prepopulated_fields ={'slug': ('name','date_of_birth')}


admin.site.register(Obituary, ObituaryAdmin)