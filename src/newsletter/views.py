from .forms import NewsletterForm
from .utils import SendSubscribeMail

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

      isSubscriptionSuccess = SendSubscribeMail(email, name)

      if isSubscriptionSuccess:
        form = NewsletterForm()
        return redirect('/potwierdzenie-zapisu/', {'form': form})
      else:
        messages.add_message(request, messages.INFO, 'Wystąpił nieoczekiwany błąd. Spróbuj ponownie.')

    else:
      messages.add_message(request, messages.WARNING, 'Błędne imię lub e-mail. Spróbuj wypełnić formularz ponownie.')



  else:
    messages.add_message(request, messages.INFO, 'Wystąpił nieoczekiwany błąd. Spróbuj ponownie.')

  form = NewsletterForm()
  return redirect(request.META['HTTP_REFERER'], {'form': form})