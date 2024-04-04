from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from api.models import Department
from api.serializers.department import DepartmentListSerializer, DepartmentRetrieveSerializer, DepartmentCreateOrUpdateSerializer


class DepartmentView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentListSerializer
        if self.action == 'retrieve':
            return DepartmentRetrieveSerializer
        if self.action == 'create':
            return DepartmentCreateOrUpdateSerializer
        if self.action == 'update':
            return DepartmentCreateOrUpdateSerializer

    def get_queryset(self):
        return Department.objects.all()