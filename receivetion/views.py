import email
import os
from django.utils import timezone
import pandas as pd
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
def invitation(request):
    return render(request,"invitation.html")

def register_user(request):

    if request.method == "POST":

        email = request.POST.get("email")
        name = request.POST.get("name")
        type = request.POST.get("type")
        reg_num = request.POST.get("reg_num")
        password = request.POST.get("password")

        pdf_path = os.path.join(settings.MEDIA_ROOT, "invitation.pdf")

        current_time = timezone.now().strftime("%d %B %Y, %I:%M %p")

        subject = "🎉 Registration Confirmed – Freshers Reception"

        message = f"""
Dear {name},


You are cordially invited to join us for a magical evening at the Fresher’s Reception 2026 🎉

Let’s come together to celebrate new beginnings, create unforgettable memories, and warmly welcome our newest members.

📅 Date: 7th April 2026
⏰ Time: 5:00 PM – 8:30 PM
📍 Venue: Auditorium, University of Asia Pacific

✨ Whether you are a Fresher, Volunteer, or Attendee — your presence will make this event even more special.



We look forward to celebrating with you!

Warm regards,
Organizing Team
Batch 56 & 57
University of Asia Pacific

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


def permession_mail(request):
    
    file_path = os.path.join(settings.MEDIA_ROOT, "CR_lists.xlsx")
    
    df = pd.read_excel(file_path)
    
    for _, row in df.iterrows():
        
        club = row['Club']
        name = row['Name']
        email = row['Email']

        subject = "Invitation to Participate in the Fresher’s Reception – Spring 2025 (Batch 58)" 
        
        message = f"""
Assalamu Alaikum Respected {club} President,

Warm greetings from   Oniruddho 56 and Riddik57 on the occasion of the Fresher’s Reception for Batch 58.

It is both our honor and delight to extend this cordial invitation to the {club} CSE to join us in welcoming the newest members of our department. The dynamic presence and contributions of your club have long been an integral part of our campus culture, and we deeply value the inspiration and energy you continue to share with the community.

Date: 7th April 2026
Time: 6:30 PM
Venue: Auditorium

As part of the program, we are delighted to host a Club Introduction Segment, where each club will be given the opportunity to present itself to the incoming students. This will be a meaningful platform to highlight your club’s journey, legacy, and achievements, while also encouraging freshers to discover the communities they may one day take pride in joining.

You are welcome to present your club through a short video, slideshow, or any other creative medium. To ensure smooth coordination and accommodate all participating clubs, we kindly request that each presentation remain within 3–4 minutes. We sincerely appreciate your cooperation in helping us maintain the rhythm of the event.

We truly hope the  {club} CSE will honor us with its presence and participation, making the reception more engaging, memorable, and inspiring for our new batch. Should you require any technical assistance or have specific requirements for your presentation, please feel free to reach out to us in advance.

With profound regards and heartfelt appreciation,

 Oniruddho 56 and Riddik 57
Organizers, Fresher’s Reception – fall 2025
"""

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    return render(request, "success.html")



def take_idea(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        idea = request.POST.get("idea")

        # Here you can save the idea to the database or send it via email

        return HttpResponse("Thank you for your idea!")
    else:
        return redirect("ideas")
    

def send_cr_mail(request):

    file_path = os.path.join(settings.MEDIA_ROOT, "CR_lists.xlsx")
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        name = row['Name']
        email = row['Email']
        club = row['Club']

        subject = "Invitation to senior CR for the freshers reception"

        message = f"""
Hello {name} vai,

You are invited to the Freshers Reception.

Regards,
Club President
"""

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    return HttpResponse("Emails sent successfully!")

def send_bachmate_mail(request):

    file_path = os.path.join(settings.MEDIA_ROOT, "CR_lists.xlsx")
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        name = row['Name']
        email = row['Email']
        club = row['Club']

        subject = "Invitation to senior CR for the freshers reception"

        message = f"""
Hello {name} vai,

You are invited to the Freshers Reception.

Regards,
Club President
"""

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    return HttpResponse("Emails sent successfully!")


def club_invitation(request):

    file_path = os.path.join(settings.MEDIA_ROOT, "CR_lists.xlsx") 
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        name = row['Name']
        email = row['Email']
        club = row['Club']

        subject = "Invitation to senior CR for the freshers reception"

        message = f"""
Assalamu Alaikum Respected {club} President,

Warm greetings from   Oniruddho 56 and Riddik57 on the occasion of the Fresher’s Reception for Batch 58.

It is both our honor and delight to extend this cordial invitation to the {club} CSE to join us in welcoming the newest members of our department. The dynamic presence and contributions of your club have long been an integral part of our campus culture, and we deeply value the inspiration and energy you continue to share with the community.

Date: 7th April 2026
Time: 6:30 PM
Venue: Auditorium

As part of the program, we are delighted to host a Club Introduction Segment, where each club will be given the opportunity to present itself to the incoming students. This will be a meaningful platform to highlight your club’s journey, legacy, and achievements, while also encouraging freshers to discover the communities they may one day take pride in joining.

You are welcome to present your club through a short video, slideshow, or any other creative medium. To ensure smooth coordination and accommodate all participating clubs, we kindly request that each presentation remain within 3–4 minutes. We sincerely appreciate your cooperation in helping us maintain the rhythm of the event.

We truly hope the  {club} CSE will honor us with its presence and participation, making the reception more engaging, memorable, and inspiring for our new batch. Should you require any technical assistance or have specific requirements for your presentation, please feel free to reach out to us in advance.

With profound regards and heartfelt appreciation,

 Oniruddho 56 and Riddik 57
Organizers, Fresher’s Reception – fall 2025
"""
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    return render(request, "success.html")
