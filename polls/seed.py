from faker import Faker
fake = Faker()
import random
from .models import*

def create_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)     
def seed_db(n=10)->None:
    try:
        for _ in range(0, n):
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)
            student_id = f'kiran{random.randint(100, 999)}'
            department = department_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                 student_address = student_address,
                
                 )
    except Exception as e:
        print(e)