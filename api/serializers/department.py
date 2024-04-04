from rest_framework import serializers
from api.models import Department


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'