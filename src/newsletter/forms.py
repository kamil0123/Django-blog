from django import forms

class NewsletterForm(forms.Form):
  name = forms.CharField(
    label='', 
    widget = forms.TextInput()
    )
  email = forms.EmailField(
    label='', 
    widget = forms.TextInput()
    )