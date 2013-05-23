# -*-coding:utf-8-*- 
from django.contrib import admin
from polls.models import Poll
from polls.models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('question',               {'fields': ['question']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')   
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
     
#admin.site.register(Poll)
#admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)