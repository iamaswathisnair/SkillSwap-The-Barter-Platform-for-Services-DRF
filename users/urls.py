from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RegisterView
from .views import NDAViewSet, NDAAcceptanceViewSet
from .views import SensitiveAssetViewSet
from .views import LeakReportViewSet
from .views import CaseFileViewSet


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# ✅ Setup router
router = DefaultRouter()
router.register(r'ndas', NDAViewSet)
router.register(r'nda-acceptances', NDAAcceptanceViewSet)
router.register(r'sensitive-assets', SensitiveAssetViewSet)
router.register(r'reports', LeakReportViewSet)
router.register(r'cases', CaseFileViewSet)



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

