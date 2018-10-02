from .forms import ContactForm

from django.conf import settings

from django.contrib import messages

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def contactView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          # redirect to a new URL:
          message = 'imie: ' + request.POST.get('name') + '\nemail: ' + request.POST.get('email') + '\n\n' + request.POST.get('message')
          send_mail(

            request.POST.get('subject'),
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
          )
          messages.add_message(request, messages.INFO, 'Dziękuję, Twoja wiadomość została wysłana.')
          # return HttpResponseRedirect('/kontakt') 


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})