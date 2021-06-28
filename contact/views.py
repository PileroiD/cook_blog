from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView

from . import forms, models


class ContactView(View):
    def get(self, request):
        contacts = models.ContactLink.objects.all()  # берем все экземпляры(иконки и их названия)
        form = forms.ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})

# class ContactView(ListView):
#     model = models.ContactModel
#     template_name = 'contact/contact.html'


class CreateContact(CreateView):
    form_class = forms.ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = models.About.objects.first()
        return render(request, 'contact/about.html', {'about': about})