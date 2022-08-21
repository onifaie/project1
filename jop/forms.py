from dataclasses import field
from pyexpat import model
from sqlite3 import DateFromTicks
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django import forms 
from . models import Kindjop,CityJop,Cetivcation,LookingJop 

class form_kindjop(forms.ModelForm):
        summary_course = forms.CharField(label='اسم الكورس ',widget=SummernoteWidget())  # instead of forms.Textarea


        class Meta:
                 model = Kindjop 
                 fields='__all__'
                  
       
        
       
       
       
class form_CityJop(forms.ModelForm):
     class Meta:
        model = CityJop 
        fields='__all__'
     
class form_comment(forms.ModelForm):
     class Meta:
        model = comment_lesson 
        fields='__all__'
        
        
class form_Cetivcation(forms.ModelForm):
     class Meta:
        model = Cetivcation
        
        fields='__all__'
        

class form_LookingJop(forms.ModelForm):
     memo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
#      memo = forms.CharField(widget=DateFromTicks())
#       
     class Meta:
        model = LookingJop
        
        fields='__all__'
        # instead of forms.Textarea

     


# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

# If you don't like <iframe>, then use inplace widget
# Or if you're using django-crispy-forms, please use this.
class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())
     