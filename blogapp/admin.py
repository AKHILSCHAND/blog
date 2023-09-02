from django.contrib import admin
from . models import *

# Register your models here.

class blogAdmin(admin .ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','status','is_featured')
    search_fields = ('id','category__category_name','status','title')
    list_editable =('is_featured',)

admin.site.register(category)
admin.site.register(blogs, blogAdmin)