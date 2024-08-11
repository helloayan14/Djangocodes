from django.contrib import admin
from .models import Chaivariety,chaireview,certificate,stores
# Register your models here.

class chaireviewinline(admin.TabularInline):
    model=chaireview
    extra=2

class chaivarietyadmin(admin.ModelAdmin):
    list_display= ('name','type','date',)
    inlines=[chaireviewinline]

class storeadmin(admin.ModelAdmin):
    list_display=('name','location',)        
    filter_horizontal=('chai_variety',)

class certifyadmin(admin.ModelAdmin):
    list_display=('chai','certify_number',)    
admin.site.register(Chaivariety,chaivarietyadmin)
admin.site.register(stores,storeadmin)
admin.site.register(certificate,certifyadmin)



