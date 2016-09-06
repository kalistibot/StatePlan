from django import forms

from .models import TMACSP_record

class SearchForm(forms.ModelForm):
    subject = forms.CharField(label='Subject_Population',max_length=100,)
    program = forms.CharField(label='Program_Category',max_length=50,)
    class Meta:
        model = TMACSP_record
        fields = ('Subject_Population', 'Program_Category',)