from django.shortcuts import render
from django.conf import settings
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_brevo_email(subject, message, to_email, to_name="User"):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key["api-key"] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    sender = {
        "name": "NexGen Tax Consultancy",
        "email": settings.DEFAULT_FROM_EMAIL,
    }

    receiver = [
        {
            "email": to_email,
            "name": to_name,
        }
    ]

    email_data = sib_api_v3_sdk.SendSmtpEmail(
        sender=sender,
        to=receiver,
        subject=subject,
        html_content=f"<pre>{message}</pre>",
    )

    try:
        api_instance.send_transac_email(email_data)
        return True
    except ApiException as e:
        print("BREVO EMAIL ERROR:", e)
        return False


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        admin_message = f"""
New Contact Request

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""

        user_message = f"""
Hello {name},

Thank you for contacting NexGen Tax Consultancy.

We have received your message successfully.
Our team will contact you shortly.

Regards,
NexGen Tax Consultancy
"""

        send_brevo_email(
            "New Contact Message",
            admin_message,
            "nexgentax2025@gmail.com",
            "Admin",
        )

        send_brevo_email(
            "Message Received - NexGen Tax Consultancy",
            user_message,
            email,
            name,
        )

        return render(request, "index.html", {"contact_success": True})

    return render(request, "index.html")


def booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        message = request.POST.get("message")

        admin_message = f"""
New Booking Received

Name: {name}
Email: {email}
Phone: {phone}
Date: {date}

Requirement:
{message}
"""

        user_message = f"""
Hello {name},

Your consultation booking is confirmed.

Date: {date}
Phone: {phone}

Our team will contact you shortly.

Thank you for choosing NexGen Tax Consultancy.

Regards,
NexGen Tax Consultancy
"""

        send_brevo_email(
            "New Consultation Booking",
            admin_message,
            "nexgentax2025@gmail.com",
            "Admin",
        )

        send_brevo_email(
            "Booking Confirmed - NexGen Tax Consultancy",
            user_message,
            email,
            name,
        )

        return render(request, "booking.html", {"success": True})

    return render(request, "booking.html")


def services(request):
    return render(request, "services.html")