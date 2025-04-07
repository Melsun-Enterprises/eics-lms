from django.shortcuts import render
from .models import Student, Course

def student_dashboard(request):
    student = Student.objects.first()  # You can filter based on the logged-in student
    courses = Course.objects.all()
    return render(request, 'dashboard/student_dashboard.html', {'student': student, 'courses': courses})

def teacher_dashboard(request):
    courses = Course.objects.all()
    return render(request, 'dashboard/teacher_dashboard.html', {'courses': courses})
