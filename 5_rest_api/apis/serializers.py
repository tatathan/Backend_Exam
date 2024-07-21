from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation']

class SchoolDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classrooms_count', 'teachers_count', 'students_count']

    def get_classrooms_count(self, obj):
        return Classroom.objects.filter(school=obj).count()

    def get_teachers_count(self, obj):
        return Teacher.objects.filter(school=obj).count()

    def get_students_count(self, obj):
        return Student.objects.filter(school=obj).count()
    
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "year", "room"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'sex']

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ("id", "first_name", "last_name", "sex")

class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, source='teacher_set')
    students = StudentSerializer(many=True)
    school = SchoolSerializer()

    class Meta:
        model = Classroom
        fields = ['id', 'year', 'room', 'school', 'teachers', 'students']

class TeacherDetailSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    # school = serializers.CharField(source='school.name')
    classroom = ClassroomSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ("id", "first_name", "last_name", "sex", "school", "classroom")


class StudentDetailSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    classroom = ClassroomSerializer()

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "sex", "school", "classroom")
