#todo>forms.py code
from django import forms
from .models import Diaries

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diaries
        fields = ('title', 'contents', 'writer')