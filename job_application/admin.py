from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('first_Name', 'last_Name', 'email')
    search_fields = ('first_Name', 'last_Name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('first_Name',)
    readonly_fields = ('occupation',)

admin.site.register(Form, FormAdmin)


