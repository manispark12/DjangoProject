import os
import django
import sys
from faker import Faker
#from datetime from datetime

sys.path.append("D://my_django_project//myDjangoProject")
#setup django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjangoProject.settings')
django.setup()

#import the model
from myDjangoSecond_app2.models import Student
#populate script

fake = Faker()

def create_students(n=50):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        course_name = "Django Training"
        enrollment_date = fake.date_between(start_date = '-30d', end_date = 'today')




        Student.objects.create(
            first_name = first_name,
            last_name=last_name,
            email=email,
            course_name = course_name,
            enrollment_date = enrollment_date
        )

if __name__ == '__main__':
    print("Populating the database with students data...")
    create_students(50)
    print("Database populated successfully...")