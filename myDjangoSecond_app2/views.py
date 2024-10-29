from django.shortcuts import HttpResponse, render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome To Django Training At CareerBridge")

def index(request):
    our_dict={'insert_myDjangoSecond':"welcome to the Django training coming from views.py file!"}
    return render(request,'myDjangoSecond_app2/index.html',context=our_dict)

def student_table(request):
    students = Student.objects.all()
    return render(request, 'myDjangoSecond_app2/student_table.html',{'students':students})

