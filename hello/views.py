from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


def get_index(request):
    return render(request, 'index.html')

def get_contact(request):
    return render(request, 'contact.html')

def get_about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def profile(request):

    return render(request, 'profile.html')