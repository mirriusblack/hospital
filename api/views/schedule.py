from rest_framework import mixins, filters
from api.models import Schedule
from api.serializers.schedule import ScheduleListSerializer, ScheduleRetrieveSerializer, ScheduleCreateOrUpdateSerializer
from api.mixin import HospitalGenericViewSet


class ScheduleView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_schedule']
        elif self.action == 'create':
            self.action_permissions = ['add_schedule']
        elif self.action == 'update':
            self.action_permissions = ['change_schedule']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_schedule']

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        if self.action == 'retrieve':
            return ScheduleRetrieveSerializer
        if self.action == 'create':
            return ScheduleCreateOrUpdateSerializer
        if self.action == 'update':
            return ScheduleCreateOrUpdateSerializer

    def get_queryset(self):
        return Schedule.objects.all()