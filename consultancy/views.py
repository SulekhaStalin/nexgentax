from django.shortcuts import render
from django.core.mail import get_connection, EmailMessage
from django.conf import settings


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
            connection = get_connection()
            connection.open()

            admin_mail = EmailMessage(
                subject='New Contact Message',
                body=f'''
New Contact Request

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['sulekhastalin2006@gmail.com'],
                connection=connection,
            )

            user_mail = EmailMessage(
                subject='Message Received - NexGen Tax Consultancy',
                body=f'''
Hello {name},

Thank you for contacting NexGen Tax Consultancy.

We have received your message successfully.
Our team will contact you shortly.

Regards,
NexGen Tax Consultancy
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
                connection=connection,
            )

            admin_mail.send()
            user_mail.send()
            connection.close()

        except Exception as e:
            print("EMAIL ERROR:", type(e).__name__, e)

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

        try:
            connection = get_connection()
            connection.open()

            admin_mail = EmailMessage(
                subject='New Consultation Booking',
                body=f'''
New Booking Received

Name: {name}
Email: {email}
Phone: {phone}
Date: {date}

Requirement:
{message}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['sulekhastalin2006@gmail.com'],
                connection=connection,
            )

            user_mail = EmailMessage(
                subject='Booking Confirmed - NexGen Tax Consultancy',
                body=f'''
Hello {name},

Your consultation booking is confirmed.

Date: {date}
Phone: {phone}

Our team will contact you shortly.

Thank you for choosing NexGen Tax Consultancy.

Regards,
NexGen Tax Consultancy
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
                connection=connection,
            )

            admin_mail.send()
            user_mail.send()
            connection.close()

        except Exception as e:
            print("EMAIL ERROR:", type(e).__name__, e)

        return render(request, 'booking.html', {
            'success': True
        })

    return render(request, 'booking.html')


def services(request):
    return render(request, 'services.html')