from rest_framework import serializers
from api.models import Visit, Schedule
from rest_framework.exceptions import ValidationError


class VisitCreateSerializer(serializers.ModelSerializer):

    def validate_schedule(self, value):
        visit_count = value.visits.count()
        print(visit_count)
        if 3 <= visit_count:
            raise ValidationError('Maximum number of entries exceeded.')
        return value


    class Meta:
        model = Visit
        fields = ['patient', 'procedure', 'schedule']


class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Visit
        fields = ['rating']