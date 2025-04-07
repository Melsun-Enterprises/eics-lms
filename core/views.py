# core/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, StudentProfile, TeacherProfile, Quiz, Question, Answer, Assignment, Event, Notification, Course, Enrollment, Grade, CourseAttachment, ContentDrip
from .forms import PaymentForm, QuizForm, QuestionForm, AnswerForm, AssignmentForm

@login_required
def dashboard(request):
    if request.user.is_student:
        return render(request, 'dashboard/student_dashboard.html')
    elif request.user.is_teacher:
        return render(request, 'dashboard/teacher_dashboard.html')
    else:
        return redirect('home')

def payment_view(request):
    message = ''
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            adm = form.cleaned_data['admission_number']
            amount = form.cleaned_data['amount']
            student = get_object_or_404(StudentProfile, admission_number=adm)
            transaction_id = f"EICS-{uuid.uuid4().hex[:8]}"

            Payment.objects.create(
                student=student,
                amount=amount,
                transaction_id=transaction_id
            )

            message = f"Payment request for KES {amount} received for {student.user.get_full_name()}. Transaction ID: {transaction_id}"

            return redirect('payment_success', transaction_id=transaction_id)
    else:
        form = PaymentForm()

    return render(request, 'payment/payment.html', {'form': form, 'message': message})

def payment_success(request, transaction_id):
    payment = get_object_or_404(Payment, transaction_id=transaction_id)
    return render(request, 'payment/payment_success.html', {'payment': payment})

    # core/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')