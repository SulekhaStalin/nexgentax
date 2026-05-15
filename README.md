NexGen Tax Consultancy Website

A professional and responsive tax consultancy website developed using Django, HTML, CSS, and JavaScript.

🌐 Live Website

https://nexgentax.onrender.com/

📌 Features
Professional responsive UI design
Consultation booking system
Contact form with email integration
Services showcase page
Interactive chatbot UI
Testimonials slider
Mobile responsive design
Modern animations and gradients
Secure deployment on Render
🛠 Technologies Used
Python
Django
HTML5
CSS3
JavaScript
WhiteNoise
Gunicorn
Render Deployment
📂 Project Structure
TaxConsultancy/
│
├── consultancy/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── TaxConsultancy/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt
🚀 Installation
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
2️⃣ Navigate to Project
cd TaxConsultancy
3️⃣ Create Virtual Environment
python -m venv venv
4️⃣ Activate Virtual Environment
Mac/Linux
source venv/bin/activate
Windows
venv\Scripts\activate
5️⃣ Install Dependencies
pip install -r requirements.txt
6️⃣ Run Migrations
python manage.py migrate
7️⃣ Start Server
python manage.py runserver
🌍 Deployment (Render)
Build Command
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start Command
gunicorn TaxConsultancy.wsgi
📧 Email Integration

SMTP email functionality is integrated for:

Contact form submissions
Consultation booking confirmations
📱 Responsive Design

The website is fully responsive and optimized for:

Desktop
Tablet
Mobile devices
👩‍💻 Developed By

Sulekha Stalin

📜 License

This project is developed for educational and professional portfolio purposes.
