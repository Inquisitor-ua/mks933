from django.contrib import admin
from .models import News, Schoolclasses, Customuser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(News)
admin.site.register(Schoolclasses)

class CustomuserAdmin(admin.ModelAdmin):
    model = Customuser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('biography', 'phone_number', 'birthday_date')}),
        )
    

admin.site.register(Customuser, CustomuserAdmin)

