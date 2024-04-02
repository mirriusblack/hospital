from rest_framework import serializers
from api.models import Specialization


class SpecializationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SpecializationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SpecializationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SpecializationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'
