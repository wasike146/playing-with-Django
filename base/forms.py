from tkinter import Widget
from xml.dom.minidom import Attr
from xml.parsers.expat import model
from django import forms
from django.forms import ModelForm
from .models import userData
from django.contrib.auth.forms import User


class userForm(forms.ModelForm):
    class Meta:
        model=userData
        fields=('fname','secordName','email_field','phoneNo')

        def __init__(self, *args, **kwargs):
            super(userForm, self).__init__(*args, **kwargs)
            self.fields['fname'].widget.attrs.update({'class': 'form-control'})
            self.fields['secordName'].widget.attrs.update({'class': 'form-control'})
            self.fields['email_field'].widget.attrs.update({'class': 'form-control'})
            self.fields['phoneNo'].widget.attrs.update({'class': 'form-control'})
