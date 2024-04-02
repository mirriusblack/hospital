from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from api.models import Procedure
from api.serializers.procedure import ProcedureListSerializer, ProcedureRetrieveSerializer, \
    ProcedureCreateSerializer, ProcedureUpdateSerializer


class ProcedureView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProcedureListSerializer
        if self.action == 'retrieve':
            return ProcedureRetrieveSerializer
        if self.action == 'create':
            return ProcedureCreateSerializer
        if self.action == 'update':
            return ProcedureUpdateSerializer

    def get_queryset(self):
        return Procedure.objects.all()