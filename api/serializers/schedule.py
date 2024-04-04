from rest_framework import serializers
from api.models import Schedule
from rest_framework.exceptions import ValidationError



class ScheduleCreateOrUpdateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)

        timestamp_start, timestamp_end = attrs['timestamp_start'], attrs['timestamp_end']

        exists = Schedule.objects.filter(
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_end
        ).exists()

        if exists:
            raise ValidationError('Schedule overlay.')

    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'