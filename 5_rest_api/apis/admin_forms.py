from django import forms
from .models import Teacher, Student

class TeacherAdminForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_classroom(self):
        classrooms = self.cleaned_data.get('classroom')
        school = self.cleaned_data.get('school')
        for classroom in classrooms:
            if classroom.school != school:
                raise forms.ValidationError(f"Classroom {classroom} must belong to the same school as the teacher.")
        return classrooms

class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_classroom(self):
        classroom = self.cleaned_data.get('classroom')
        school = self.cleaned_data.get('school')
        if classroom and classroom.school != school:
            raise forms.ValidationError(f"Classroom {classroom} must belong to the same school as the student.")
        return classroom