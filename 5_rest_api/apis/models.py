from django.db import models

class School(models.Model):
    name = models.CharField(max_length=300)
    abbreviation = models.CharField(max_length=10)
    address = models.TextField()
     
    def __str__(self):
        return self.name
    
class Classroom(models.Model):
    year = models.PositiveIntegerField()
    room = models.CharField(max_length=2)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
     
    def __str__(self):
        return f"{self.year}/{self.room} {self.school.name}"
    
class Person(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
    
class Teacher(Person):
    classroom = models.ManyToManyField(Classroom, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(Person):
    classroom = models.ForeignKey(Classroom, related_name="students", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
