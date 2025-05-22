from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import NDA, NDAAcceptance
from .serializers import NDASerializer, NDAAcceptanceSerializer
from .permissions import IsCompanyOwnerOnly

from .models import SensitiveAsset
from .serializers import SensitiveAssetSerializer

from .models import LeakReport
from .serializers import LeakReportSerializer

from .models import CaseFile
from .serializers import CaseFileSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    



# 🔐 NDA ViewSets
class NDAViewSet(viewsets.ModelViewSet):
    queryset = NDA.objects.all()
    serializer_class = NDASerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOnly]


class NDAAcceptanceViewSet(viewsets.ModelViewSet):
    queryset = NDAAcceptance.objects.all()
    serializer_class = NDAAcceptanceSerializer
    permission_classes = [IsAuthenticated]


# 🛡️ Sensitive Asset ViewSet
class SensitiveAssetViewSet(viewsets.ModelViewSet):
    queryset = SensitiveAsset.objects.all()
    serializer_class = SensitiveAssetSerializer
    permission_classes = [IsAuthenticated]


# 🕵️ Leak Report ViewSet
class LeakReportViewSet(viewsets.ModelViewSet):
    queryset = LeakReport.objects.all()
    serializer_class = LeakReportSerializer
    permission_classes = [IsAuthenticated]


# 📂 Case File ViewSet
class CaseFileViewSet(viewsets.ModelViewSet):
    queryset = CaseFile.objects.all()
    serializer_class = CaseFileSerializer
    permission_classes = [IsAuthenticated]

