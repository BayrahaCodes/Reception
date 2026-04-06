import os
from django.utils import timezone

from django.shortcuts import redirect, render
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.http import HttpResponse
from receivetion.models import Attendee 

# required import

def home(request):
    return render(request, "index.html")
def register(request):
    return render(request, "register.html")
def events(request):
    return render(request, "events.html")

def gallery(request):
    return render(request, "gellary.html")

def ideas(request):
    return render(request, "idea.html")

def contact(request):
    return render(request, "contacts.html")

def success(request):
    return render(request, "success.html")

def register_user(request):

    if request.method == "POST":

        email = request.POST.get("email")
        name = request.POST.get("name")
        type = request.POST.get("type")
        reg_num = request.POST.get("reg_num")
        password = request.POST.get("password")

        pdf_path = os.path.join(settings.MEDIA_ROOT, "schedule.pdf")

        current_time = timezone.now().strftime("%d %B %Y, %I:%M %p")

        subject = "🎉 Confirmation and Invitation – Fresher’s Receptionn"

        message = f"""

Dear {name},

We are pleased to confirm your successful registration for the upcoming Fresher’s Reception. It is with great pleasure that we cordially invite you to attend this special event, where we look forward to welcoming you and celebrating together.

Please find the attached PDF file containing your confirmation details and relevant event information. We kindly request you to review the document and keep it for reference.

Your presence will greatly enhance the occasion, and we sincerely hope you will be able to join us.

Should you have any questions or require further assistance, please feel free to contact us.

Thank you for your registration. We look forward to seeing you at the event.

Warm regards,
 Batch 56 & 57.

📅 Registration Time:
{current_time}
"""

        try:

            # save data
            Attendee.objects.create(
                name=name,
                email=email,
                type=type,
                reg_number=reg_num,
                password=password
            )

            # send email
            email_message = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )

            email_message.attach_file(pdf_path)
            email_message.send()

            return redirect("success")

        except Exception as e:
            print(e)
            return redirect("register")

    return redirect("register")
