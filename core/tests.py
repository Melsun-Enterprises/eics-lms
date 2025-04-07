# core/tests.py
from django.test import TestCase
from .models import StudentProfile, TeacherProfile, Quiz, Question, Answer, Assignment, Event, Notification

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.student_profile = StudentProfile.objects.create(user=self.user, admission_number='12345')
        self.teacher_profile = TeacherProfile.objects.create(user=self.user)
        self.quiz = Quiz.objects.create(title='Test Quiz', description='A test quiz', created_by=self.user)
        self.question = Question.objects.create(quiz=self.quiz, text='Test Question')
        self.answer = Answer.objects.create(question=self.question, text='Test Answer', is_correct=True)
        self.assignment = Assignment.objects.create(title='Test Assignment', description='A test assignment', created_by=self.user)
        self.event = Event.objects.create(title='Test Event', description='A test event', start_time='2023-01-01 00:00:00', end_time='2023-01-01 01:00:00', created_by=self.user)
        self.notification = Notification.objects.create(user=self.user, message='Test Notification')

    def test_models(self):
        self.assertEqual(self.student_profile.__str__(), f"{self.user.get_full_name()} (12345)")
        self.assertEqual(self.teacher_profile.__str__(), self.user.get_full_name())
        self.assertEqual(self.quiz.__str__(), 'Test Quiz')
        self.assertEqual(self.question.__str__(), 'Test Question')
        self.assertEqual(self.answer.__str__(), 'Test Answer')
        self.assertEqual(self.assignment.__str__(), 'Test Assignment')
        self.assertEqual(self.event.__str__(), 'Test Event')
        self.assertEqual(self.notification.__str__(), f"Notification for {self.user.get_full_name()}")