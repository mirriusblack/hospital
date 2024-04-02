from rest_framework import serializers
from api.models import Procedure


class ProcedureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class ProcedureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class ProcedureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class ProcedureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'