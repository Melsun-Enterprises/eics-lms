# 🎓 EICS LMS — Learn. Grow. Get Hired.

Welcome to the official Learning Management System (LMS) for **Emmanuel Institute of Certified Studies (EICS)** — a future-forward digital learning platform built with Django 5.

[🔗 View on GitHub](https://github.com/Melsun-Enterprises/eics-lms)

---

## 🚀 Key Features

- 📚 **Course Management** — Lecturers can easily upload, manage, and organize course content.
- 🧑‍🎓 **Student Dashboards** — Personalized dashboards with progress tracking and notifications.
- 📅 **Interactive Calendar** — Stay on top of classes, exams, and events.
- 💳 **Secure M-PESA Payments** — Powered by Paybill `4080793`. Use your admission number as the account.
- 📈 **Analytics & Insights** — Real-time stats on attendance, grades, and more.
- 🔔 **Notification System** — Stay updated without missing a beat.
- 🛠️ **Admin Panel** — Powerful, intuitive controls for staff and management.

---

## 💼 The Freelancer Tab (Beta)

All students will be **automatically added** to a new **Freelancer** tab within the LMS.

> 🎯 This boosts visibility and helps students land real jobs, gigs, or side hustles with ease.

Hiring? Just browse the Freelancer tab.  
A student? Your profile does the talking.

Say less. Work more.

---

## ⚙️ Tech Stack

- Django 5.2
- Gunicorn
- PostgreSQL
- HTML5, TailwindCSS
- Render (for deployment)
- M-PESA API Integration (Lipa na M-PESA)

---

## 📦 Local Setup

```bash
git clone https://github.com/Melsun-Enterprises/eics-lms.git
cd eics-lms
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🧠 Dev Notes
Set up your .env for secrets and M-PESA keys.

Create a superuser with python manage.py createsuperuser.

Admin path: /admin/ – keep it safe.
🙌 Contributing
Pull requests are welcome. Feedback is golden.
Whether you're a student or alumni — this platform is yours too.
🧾 License
MIT License.
Built by EICS.
Crafted for learners.
Tuned for impact.

