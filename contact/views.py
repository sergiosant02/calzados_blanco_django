from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from django.core.mail import EmailMessage

from django.conf import settings

# Create your views here.

def contact(request):
    if request.method=="GET":
        contact_form = ContactForm()
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            content = form.cleaned_data["content"]
            
            body = "El usuario con nombre {} e email {}, escribe:\n\n {}".format(name, email, content)
            email = EmailMessage("mensaje desde app django", body, "", ["sergiosantiago0403@gmail.com"], reply_to=[email])
            
            try:
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?noValid')
    return render(request, 'contact/contact.html', {'form': contact_form})