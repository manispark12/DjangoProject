from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    course_name = models.CharField(default="Django Training", max_length=50)
    enrollment_date = models.DateField(auto_now_add=True)

def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.course}"