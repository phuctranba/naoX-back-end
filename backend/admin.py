from django.contrib import admin
from .models import UnitAnalysis, AnalysisResults, Campaign, Cumstomer, Notification
# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    list_display = ['ID']

class CumstomerAdmin(admin.ModelAdmin):
    list_display = ['ID']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['ID']

class UnitAnalysisAdmin(admin.ModelAdmin):
    list_display = ['ID', 'NAME', 'KEY_MAIN', 'ACTIVE', 'KEY_EXTRA']
    search_fields = ['KEY_MAIN']

class AnalysisResultsAdmin(admin.ModelAdmin):
    list_display = ['ID', 'POSITIVE_INDICATOR', 'NEGATIVE_INDICATOR']
    search_fields = ['POSITIVE_INDICATOR', 'NEGATIVE_INDICATOR']

admin.site.register(UnitAnalysis, UnitAnalysisAdmin)
admin.site.register(AnalysisResults, AnalysisResultsAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Cumstomer, CumstomerAdmin)
admin.site.register(Notification, NotificationAdmin)