from django.contrib import admin

# Register your models here.
from .models import Couses


class CousesAdmin(admin.ModelAdmin):
    list_display = ("id","subject","term","couseid","num_student","year",)



admin.site.register(Couses , CousesAdmin)
