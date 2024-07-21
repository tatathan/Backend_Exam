from rest_framework import viewsets, permissions
from apis.models import School
from apis.serializers import SchoolDetailSerializer
from apis.filters import SchoolFilter
from django_filters.rest_framework import DjangoFilterBackend


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SchoolDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter