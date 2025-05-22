from rest_framework import serializers
from .models import CustomUser ,NDAAcceptance,CaseFile,LeakReport,SensitiveAsset,NDA

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    
# 📄 NDA SERIALIZER
class NDASerializer(serializers.ModelSerializer):
    assigned_employees = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.filter(role='employee')
    ) #Dear DRF, when sending/receiving NDA data, just show me the employee IDs (primary keys).”

    class Meta:
        model = NDA
        fields = '__all__'


# 🧠 SENSITIVE ASSET SERIALIZER
class SensitiveAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensitiveAsset
        fields = '__all__'


# 🚨 LEAK REPORT SERIALIZER
class LeakReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeakReport
        fields = '__all__'


# 📂 CASE FILE SERIALIZER
class CaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseFile
        fields = '__all__'
