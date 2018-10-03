from .forms import NewsletterForm

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def newsletterSubscribe(request):

  if request.method == "POST":
    form = NewsletterForm(request.POST)  

    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      print(name)
      print(email)

      messages.add_message(request, messages.INFO, 'Dziękuję, zostałeś zapisany.')
    else:

      messages.add_message(request, messages.WARNING, 'Błędne imię lub hasło. Spróbuj wypełnić formularz ponownie.')

  else:

    messages.add_message(request, messages.INFO, 'Wystąpił nieoczekiwany błąd. Spróbuj ponownie.')
    form = NewsletterForm()

  return redirect(request.META['HTTP_REFERER'], {'form': form})