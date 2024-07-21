from django_filters import FilterSet
from .models import School, Classroom, Teacher, Student


class SchoolFilter(FilterSet):

    class Meta:
        model = School
        fields = {
            "name": ['exact', 'icontains'],
        }

class ClassroomFilter(FilterSet):

    class Meta:
        model = Classroom
        fields = {
            "school": ['exact'],
        }

class TeacherFilter(FilterSet):

    class Meta:
        model = Teacher
        fields = {
            "school": ['exact'],
            "classroom": ['exact'],
            "first_name": ['exact'],
            "last_name": ['exact'],
            "sex": ['exact'],
        }

class StudentFilter(FilterSet):

    class Meta:
        model = Student
        fields = {
            "school": ['exact'],
            "classroom": ['exact'],
            "first_name": ['exact'],
            "last_name": ['exact'],
            "sex": ['exact'],
        }
