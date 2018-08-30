from django import forms


class ContactForm(forms.Form):
  name = forms.CharField(
    label='', 
    widget = forms.TextInput(
      attrs={
        "class": "col-sm-12 name-input",
        "placeholder": "Imię"}
      )
    )
  email = forms.EmailField(
    label='', 
    widget = forms.TextInput(
      attrs={
        "class": "col-sm-12 email-input",
        "placeholder": "Email"}
      )
    )
  subject = forms.CharField(
    label='', 
    widget = forms.TextInput(
      attrs={
        "class": "col-sm-12 subject-input",
        "placeholder": "Tytuł"}
      )
    )
  message = forms.CharField(
    label='', 
    widget = forms.Textarea(
      attrs={
        "class": "col-sm-12 message-input",
        "placeholder": "Wiadmość", 
        "rows": 6}
      )
    ) 