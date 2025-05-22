from django.contrib import admin
from .models import CustomUser,NDAAcceptance,CaseFile,LeakReport,SensitiveAsset,NDA


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(NDAAcceptance)
admin.site.register(CaseFile)
admin.site.register(LeakReport)
admin.site.register(SensitiveAsset)
admin.site.register(NDA)

