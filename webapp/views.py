from django.shortcuts import render
from pricingdata.models import *
from contactdata.models import *


def home(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/index.html", context)


def about(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/about.html", context)


def pricing(request):
    pricing = Pricing.objects.all()
    context = {
        'pricing': pricing
    }
    return render(request, "webpages/pricing.html", context)


def contact(request):
    phone = Phone.objects.all()
    email = Email.objects.all()
    office = Office.objects.all()
    contact = Contact.objects.all()
    context = {
        'phone': phone,
        'email': email,
        'office': office,
        'contact': contact
    }
    return render(request, "webpages/contact.html", context)


def service(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/service.html", context)


def service_detail(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/service-details.html", context)


def blog(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/blog-standard.html", context)


def blog_detail(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/blog-details.html", context)


def portfolio(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/porfolio.html", context)


def portfolio_detail(request):
    # users = User.objects.all()
    context = {
        # 'users': users
    }
    return render(request, "webpages/porfolio-details.html", context)

