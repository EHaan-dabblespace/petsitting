from django.contrib import admin
from .models import Family, Pet

# Register your models here.
admin.site.register((Family, Pet))
