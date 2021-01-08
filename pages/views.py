from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from services.models import Service
from customer.models import Testimonial
from blog.models import BlogPost

def index(request):
    about = "The Centre for Self Employment and Management Development (CSMD) Company is an indigenous business start up and management development trainer, consultant, vocational and entrepreneurship skills provider for all categories of employees and potential entrepreneurs including unemployed individuals in the society. She also caters for the needs of old workers (both the current and intending retirees)."
    services = Service.objects.all()[:2]
    services2 = Service.objects.all()[3:5]
    services3 = Service.objects.all()
    testimonials = Testimonial.objects.all()[:4]
    context = {
        "about":about,
        "services": services,
        "services2": services2,
        "services3": services3,
        "testimonials": testimonials,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    about = "The Centre for Self Employment and Management Development (CSMD) Company is an indigenous business start up and management development trainer, consultant, vocational and entrepreneurship skills provider for all categories of employees and potential entrepreneurs including unemployed individuals in the society. She also caters for the needs of old workers (both the current and intending retirees)."
    services3 = Service.objects.all()
    context = {
        "services3": services3,
        'about':about
    }
    return render(request, 'pages/about.html', context)


def services(request):
    about = "The Centre for Self Employment and Management Development (CSMD) Company is an indigenous business start up and management development trainer, consultant, vocational and entrepreneurship skills provider for all categories of employees and potential entrepreneurs including unemployed individuals in the society. She also caters for the needs of old workers (both the current and intending retirees)."
    services = Service.objects.all()
    blog = BlogPost.objects.all().order_by('-id')[:2]
    services1 = Service.objects.all()[:3]
    services2 = Service.objects.all()[3:]
    context = {
        "services3": services,
        "services2": services2,
        "services1": services1,
        'about':about,
        'blog':blog,

    }
    return render(request, 'pages/services.html', context)


def contact(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        return redirect('/')
        # send mail
        subject = 'Enquiry'
        message1 = message
        from_email = 'batmobi748@gmail.com'
        receipients = ['cutejosh2@gmail.com']
        send_mail(
            subject,
            message1,
            from_email,
            receipients,
            fail_silently=True
        )
        messages.success(
            request, 'Your message has been sent, we will get back to you')
    services = Service.objects.all()
    about = "The Centre for Self Employment and Management Development (CSMD) Company is an indigenous business start up and management development trainer, consultant, vocational and entrepreneurship skills provider for all categories of employees and potential entrepreneurs including unemployed individuals in the society. She also caters for the needs of old workers (both the current and intending retirees)."
    context = {
        "services3": services,
        'about':about,

    }
    return render(request, 'pages/contact.html', context)
