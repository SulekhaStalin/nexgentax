from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
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
                settings.DEFAULT_FROM_EMAIL,
                ['sulekhastalin2006@gmail.com'],
                fail_silently=False,
            )

            send_mail(
                'Message Received - NexGen Tax Consultancy',
                f'''
Hello {name},

Thank you for contacting NexGen Tax Consultancy.

We have received your message successfully.
Our team will contact you shortly.

Regards,
NexGen Tax Consultancy
                ''',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

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
            send_mail(
                'New Consultation Booking',
                f'''
New Booking Received

Name: {name}
Email: {email}
Phone: {phone}
Date: {date}

Requirement:
{message}
                ''',
                settings.DEFAULT_FROM_EMAIL,
                ['sulekhastalin2006@gmail.com'],
                fail_silently=False,
            )

            send_mail(
                'Booking Confirmed - NexGen Tax Consultancy',
                f'''
Hello {name},

Your consultation booking is confirmed.

Date: {date}
Phone: {phone}

Our team will contact you shortly.

Thank you for choosing NexGen Tax Consultancy.

Regards,
NexGen Tax Consultancy
                ''',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

        except Exception as e:
            print("EMAIL ERROR:", type(e).__name__, e)

        return render(request, 'booking.html', {
            'success': True
        })

    return render(request, 'booking.html')


def services(request):
    return render(request, 'services.html')