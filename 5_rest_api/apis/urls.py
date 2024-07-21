from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.student import StudentViewset
from .views.v1.teacher import TeacherViewset
from .views.v1.classroom import ClassroomViewset
from .views.v1.school import SchoolViewset


router = DefaultRouter()
router.register('schools', SchoolViewset, basename='school')
router.register('classrooms', ClassroomViewset, basename='classroom')
router.register('students', StudentViewset, basename='student')
router.register('teachers', TeacherViewset, basename='teacher')
api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
