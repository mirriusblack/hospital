from rest_framework import serializers
from api.models import Doctor


class DoctorListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()


class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'additional_info']