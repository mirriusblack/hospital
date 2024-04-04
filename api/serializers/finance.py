from rest_framework import serializers
from api.models import Finance, Procedure



class FinanceCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Finance
        fields = '__all__'


class FinanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'


class FinanceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'
