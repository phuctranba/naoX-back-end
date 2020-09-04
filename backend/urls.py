from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .serializers import UnitAnalysisSerializers
from .models import UnitAnalysis

# ViewSets define the view behavior.
class UnitAnalysisViewSet(viewsets.ModelViewSet):
    queryset = UnitAnalysis.objects.all()
    serializer_class = UnitAnalysisSerializers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'real-estate', UnitAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]