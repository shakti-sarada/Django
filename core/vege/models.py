from django.db import models
from django.contrib.auth import get_user_model
from .utils import generate_slug

User = get_user_model()

class StudentsManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted = False)

class recipe(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="recipe")
    slug = models.SlugField(unique=True)
    

    

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(recipe, self).save(*args,**kwargs) 


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
    class Meta:
        ordering = ['student_id']

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name    

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart",on_delete=models.CASCADE) 
    student_id = models.OneToOneField(StudentID, related_name="studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    objects = StudentsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name}, {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student','subject']
        ordering = ['student']


class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard", on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank','creation_date']

