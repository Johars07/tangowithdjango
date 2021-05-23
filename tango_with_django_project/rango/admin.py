from django.contrib import admin
from rango.models import Category, Page
# Register your models here.
from tango_with_django_project.rango.models import PageAdmin

admin.site.register(Category)
admin.site.register(PageAdmin)
