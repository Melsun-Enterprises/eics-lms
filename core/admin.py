# core/admin.py
from django.contrib import admin
from .models import StudentProfile, TeacherProfile, Quiz, Question, Answer, Assignment, Event, Notification

admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Assignment)
admin.site.register(Event)
admin.site.register(Notification)