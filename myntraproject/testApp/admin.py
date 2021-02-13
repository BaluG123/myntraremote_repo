from django.contrib import admin
from testApp.models import buyer

class buyeradmin(admin.ModelAdmin):
    list_display=['name','gender','location']

# Register your models here.
admin.site.register(buyer,buyeradmin)
