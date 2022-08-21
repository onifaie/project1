from dataclasses import field
from pyexpat import model
from django import forms 
from . models import blog 
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class myforms(forms.ModelForm):
      content = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

      class Meta:
        model = blog 
        fields=['title','content','add_date','image','author']
       