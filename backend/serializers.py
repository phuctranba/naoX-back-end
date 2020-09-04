from rest_framework import routers, serializers, viewsets
from .models import UnitAnalysis, Cumstomer, AnalysisResults, Campaign, Notification

class UnitAnalysisSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnitAnalysis
        fields = ['ID', 'CAMPAIGN_ID', 'NAME', 'TYPE', 'KEY_MAIN', 'KEY_EXTRA', 'KEY_EXCLUDE', 'KEY_PLACE', 'CREATE_DATE','UPDATE_DATE','VERSION','ACTIVE']