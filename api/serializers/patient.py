from rest_framework import serializers
from api.models import Patient


class PatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    birthday = serializers.DateField()
    gender = serializers.CharField()


class PatientRetrieveSerializer(PatientListSerializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    additional_info = serializers.CharField()


class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'