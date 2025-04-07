# core/forms.py

from django import forms
from .models import Quiz, Question, Answer, Assignment

class PaymentForm(forms.Form):
    admission_number = forms.CharField(label="Admission Number", required=True)
    amount = forms.DecimalField(label="Amount (KES)", max_digits=8, decimal_places=2, required=True)

    def clean_admission_number(self):
        admission_number = self.cleaned_data.get('admission_number')
        if not StudentProfile.objects.filter(admission_number=admission_number).exists():
            raise forms.ValidationError("No student found with this admission number.")
        return admission_number

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description']