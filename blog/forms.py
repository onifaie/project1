from dataclasses import field
from pyexpat import model
from django import forms 
from . models import blog 

class myforms(forms.ModelForm):
     class Meta:
        model = blog 
        fields=['title','content','add_date','image','author']
       