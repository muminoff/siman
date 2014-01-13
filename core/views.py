from django.shortcuts import render
from django.utils.translation import ugettext as _


def home_page(request):
    return render(request, 'dashboard.html')


def login_page(request):
    return render(request, 'login.html')
