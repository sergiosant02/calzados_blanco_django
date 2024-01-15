from django.shortcuts import render, HttpResponse
from django.conf import settings
# Create your views here.

def home(request):
    app_name = settings.APP_SHOW_NAME
    return render(request, 'core/home.html', {'app_name': app_name})
