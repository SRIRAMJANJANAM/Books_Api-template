from .models import *
from django import forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date'}),

        }