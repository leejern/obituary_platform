from django import forms
from .models import Obituary
from django.utils.text import slugify

class ObituaryForm(forms.ModelForm):
    class Meta: 
        model = Obituary
        fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Deceased name'}),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Birth', 'type':'date'}),
            'date_of_death': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Death', 'type':'date'}),
            'content': forms.Textarea(attrs={'class':'form-control','rows':3, 'columns':5}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author Name'}),  # Add placeholder attribute to input field
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            formatted_name = '-'.join(instance.name.split()).lower()
            formatted_dob = instance.date_of_birth.strftime('%Y-%d-%m')
            instance.slug = slugify(f'{formatted_name}-{formatted_dob}')
        if commit:
            instance.save()
        return instance
