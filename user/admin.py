from django.contrib import admin

from .models import Categorie, SubCategory
# Register your models here.

admin.site.register(Categorie)

admin.site.register(SubCategory)