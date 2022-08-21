from dataclasses import field
from pyexpat import model
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django import forms 
from . models import courses,lesson,comment_lesson,gatogery_course 

class form_course(forms.ModelForm):
        summary_course = forms.CharField(label='اسم الكورس ',widget=SummernoteWidget())  # instead of forms.Textarea


        class Meta:
                 model = courses 
                 fields='__all__'
                  
       
        
       
       
       
class form_lesson(forms.ModelForm):
     class Meta:
        model = lesson 
        fields='__all__'
     
class form_comment(forms.ModelForm):
     class Meta:
        model = comment_lesson 
        fields='__all__'
        
        
class form_gatogery(forms.ModelForm):
     class Meta:
        model = gatogery_course 
        
        fields='__all__'
        

# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

# If you don't like <iframe>, then use inplace widget
# Or if you're using django-crispy-forms, please use this.
class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())
     