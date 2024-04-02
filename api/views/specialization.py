from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, mixins
from api.models import Specialization
from api.serializers.specialization import SpecializationListSerializer, SpecializationRetrieveSerializer, \
    SpecializationCreateSerializer, SpecializationUpdateSerializer


class SpecializationView(
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
            return SpecializationListSerializer
        if self.action == 'retrieve':
            return SpecializationRetrieveSerializer
        if self.action == 'create':
            return SpecializationCreateSerializer
        if self.action == 'update':
            return SpecializationUpdateSerializer

    def get_queryset(self):
        return Specialization.objects.all()