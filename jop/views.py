from django.shortcuts import render
from django.views.generic import ListView,DetailView ,CreateView,UpdateView,DeleteView
import django.utils.timezone
from datetime import date, timedelta
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms 
from . models import Kindjop,CityJop,Cetivcation,LookingJop 

# Create your views here.

from .models  import LookingJop
def xx(request):
    context= LookingJop.objects.all()
    return render(request,'pages/mainjop.html',{'context':context})



    
class LookingJopCreate(CreateView):
    # summary_course = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    
    model=LookingJop
    template_name='CourseCreate.html'
    fields = '__all__'
    # context_object_name='courses'
    
    
class LookingJopDetails(UpdateView):
    # summary_course = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    
    model=LookingJop
    template_name='CourseCreate.html'
    fields = '__all__'
    # context_object_name='courses'
    
    
class LookingJopDelete(DeleteView):
    # summary_course = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    
    model=LookingJop
    template_name='CourseCreate.html'
    fields = '__all__'
    # context_object_name='courses'
    
    