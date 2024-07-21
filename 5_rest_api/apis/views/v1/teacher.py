from rest_framework import viewsets, permissions
from apis.models import Teacher
from apis.serializers import TeacherDetailSerializer
from apis.filters import TeacherFilter
from django_filters.rest_framework import DjangoFilterBackend


class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TeacherDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter