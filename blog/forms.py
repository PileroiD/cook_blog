from django import forms

from blog.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'website', 'massage']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email...'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website...'}),
            'massage': forms.Textarea(attrs={'placeholder': 'Your message...'}),
        }