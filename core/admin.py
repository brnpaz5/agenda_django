from django.contrib import admin
from core.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','event_date', 'creation_date')
    list_filter = ('title',)

admin.site.register(Event, EventAdmin)