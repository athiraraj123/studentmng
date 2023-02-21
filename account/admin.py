from django.contrib import admin

# Register your models here.
from .models import Course,Contact,Staff
admin.site.register(Course)
admin.site.register(Staff)

class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails)
