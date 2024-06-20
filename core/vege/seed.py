from faker import Faker
fake = Faker()
import random
from .models import *
from django.db.models import Sum

def create_subjects_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,50)
                )
    except Exception as e:
        print(e)

def seed_db(n=50) ->None:
    try:
        for _ in range(n):

            department_objs = Department.objects.all()
            random_index = random.randint(0,len(department_objs)-1)
            student_id = f'STID-0{random.randint(0,1000)}'
            department = department_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
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


from django.db import IntegrityError
from datetime import datetime
from .models import Student, ReportCard

def generate_report_card():
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', '-student_age') #Annotate Marks and Order by Marks and Age:
    i = 1
    creation_date = datetime.now().date()  # Ensuring a unique creation date for each invocation

 
# Check for Existing Records and Handle Exceptions:
    for rank in ranks:
        try:
            # Check if a record with the same student_rank and creation_date already exists
            if not ReportCard.objects.filter(student_rank=i, creation_date=creation_date).exists():
                ReportCard.objects.create(
                    student=rank,
                    student_rank=i,
                    creation_date=creation_date
                )
            else:
                print(f"Record with student_rank={i} and creation_date={creation_date} already exists.")
            
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
        
        i += 1  # Increment the rank
