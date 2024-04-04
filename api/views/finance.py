from rest_framework import mixins
from api.models import Finance
from api.serializers.finance import FinanceListSerializer, FinanceRetrieveSerializer, FinanceCreateOrUpdateSerializer
from api.mixin import HospitalGenericViewSet


class FinanceView(
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
            self.action_permissions = ['view_finance']
        elif self.action == 'create':
            self.action_permissions = ['add_finance']
        elif self.action == 'update':
            self.action_permissions = ['change_finance']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_finance']

    def get_serializer_class(self):
        if self.action == 'list':
            return FinanceListSerializer
        if self.action == 'retrieve':
            return FinanceRetrieveSerializer
        if self.action == 'create':
            return FinanceCreateOrUpdateSerializer
        if self.action == 'update':
            return FinanceCreateOrUpdateSerializer

    def get_queryset(self):
        return Finance.objects.all()
