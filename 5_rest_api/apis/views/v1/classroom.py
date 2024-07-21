from rest_framework import viewsets, permissions
from apis.models import Classroom
from apis.serializers import ClassroomDetailSerializer
from apis.filters import ClassroomFilter
from django_filters.rest_framework import DjangoFilterBackend


class ClassroomViewset(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClassroomDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter