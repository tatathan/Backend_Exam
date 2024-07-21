from rest_framework import viewsets, permissions
from apis.models import Student
from apis.serializers import StudentDetailSerializer
from apis.filters import StudentFilter
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter