from django import forms

from contact import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = '__all__'