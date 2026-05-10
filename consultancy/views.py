from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # ================= ADMIN MAIL =================

        send_mail(
            'New Contact Message',
            f'''
New Contact Request

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
            ''',
            settings.EMAIL_HOST_USER,
            ['nexgentax2025@gmail.com'],
            fail_silently=True,
        )

        # ================= USER CONFIRMATION =================

        send_mail(
            'Message Received',
            f'''
Hello {name},

Thank you for contacting NexGen Tax Consultancy.

We have received your message successfully.
Our team will contact you shortly.

Regards,
NexGen Tax Consultancy
            ''',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=True,
        )

        return render(request, 'index.html', {
            'contact_success': True
        })

    return render(request, 'index.html')


def booking(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')

        # ================= ADMIN MAIL =================

        send_mail(
            'New Consultation Booking',
            f'''
New Booking Received

Name: {name}
Email: {email}
Phone: {phone}
Consultation Date: {date}

Requirement:
{message}
            ''',
            settings.EMAIL_HOST_USER,
            ['nexgentax2025@gmail.com'],
            fail_silently=True,
        )

        # ================= USER CONFIRMATION =================

        send_mail(
            'Booking Confirmed',
            f'''
Hello {name},

Your consultation booking has been confirmed successfully.

Booking Details:
Date: {date}
Phone: {phone}

Thank you for choosing NexGen Tax Consultancy.

Regards,
NexGen Tax Consultancy
            ''',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=True,
        )

        return render(request, 'booking.html', {
            'success': True
        })

    return render(request, 'booking.html')


def services(request):
    return render(request, 'services.html')