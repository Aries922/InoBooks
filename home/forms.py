from django import  forms

from .models import Books

class uploadform(forms.ModelForm):
    class Meta :
        model = Books
        fields={'user','name','author','Description','pdf','img'}