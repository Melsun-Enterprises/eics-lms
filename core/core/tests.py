from django.test import TestCase
from .models import Student, Course

class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='John', last_name='Doe', email='john.doe@example.com', enrollment_date='2025-04-07'
        )
    
    def test_student_creation(self):
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.last_name, 'Doe')

class CourseTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Python 101', description='Introduction to Python', price=199.99
        )
    
    def test_course_creation(self):
        self.assertEqual(self.course.name, 'Python 101')
        self.assertEqual(self.course.price, 199.99)
