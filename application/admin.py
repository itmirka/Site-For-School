from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'student_name', 'student_date', 'family_name', 'contact_phone_number', 'email', 'adress')
	search_fields = ('student_name', 'student_date', 'family_name')


admin.site.register(Application, ApplicationAdmin)