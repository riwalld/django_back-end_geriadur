
from django.urls import path, include
from .views import SemanticFieldsViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', SemanticFieldsViewSet, basename='semantic_fields')

urlpatterns = [
    path('', include(router.urls)),


]
