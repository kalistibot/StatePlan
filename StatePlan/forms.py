from django import forms

from .models import Record

class SearchForm(forms.ModelForm):
    subject = forms.CharField(label='Subject',max_length=100,)
    program = forms.CharField(label='Program',max_length=50,)
    class Meta:
        model = Record
        fields = ('Subject', 'Program',)