from django.db import models
from django.contrib.auth.models import User

'''

class Employee(models.Model):
    employee_name = models.CharField(max_length=50, null=False, blank=False)
    employee_salary = models.IntegerField(null=False, blank=False)
'''
'''

class Student(models.Model):
    student_name = models.CharField(max_length=50, null=False, blank=False)
    student_age = models.IntegerField(null=False, blank=False)

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
'''
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']    

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    student_id = models.OneToOneField(StudentID, related_name="studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField()
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'

class Receipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to='receipes/')
    receipe_view_count = models.IntegerField(default=1)

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name
    
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
        unique_together = ['student','subject']
