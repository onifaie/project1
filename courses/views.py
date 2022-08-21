from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView ,CreateView
import django.utils.timezone
from datetime import date, timedelta
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms 

# Create your views here.
from django.shortcuts import render,redirect
from .models import courses,lesson,comment_lesson,gatogery_course
from .forms import form_course

def all_courses(request):
        
    course=courses.objects.all()
    form=form_course()
    return render(request, 'all_courses.html',{'course':course,'form':form})

# Create your views here.


def add_new_course(request):
     
   if request.method == "POST":
        form = form_course(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('all_courses')
   else:
        form = form_course()
   return render(request, 'add_new_course.html', {'form': form})

        
# def index(request):
#     return render(request,'index.html')

# def test (request):
#     return render(request,'test.html')



# def add_new(request):
#     if request.method == "POST":
#         form = myforms(request.POST, request.FILES)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             return redirect('all_post')
#     else:
#         form = myforms()
#     return render(request, 'add_new.html', {'form': form})





# def edit_blog(request, id):
#     band = blog.objects.get(id=id)

#     if request.method == 'POST':
#         form = myforms(request.POST,request.FILES,instance=band )
#         if form.is_valid():
#             # update the existing `Band` in the database
#             form.save()
#             # redirect to the detail page of the `Band` we just updated
#             return redirect('all_post')
#     else:
#         form = myforms(instance=band)

#     return render(request,
#                 'edit.html',
#                 {'form': form})



class CourseList(ListView):
    
    model=courses
    template_name="list.html"
    # queryset =courses.objects.filter(add_date=date.today())
    context_object_name='context'
    # context_object_name='course'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my"] = 'obeid'
        return context
    
    
    
class CouresDetail(DetailView):
    
    model=courses
    template_name='Details.html'
    # context_object_name='courses'
    
    
    
class CouresCreate(CreateView):
    # summary_course = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    
    model=courses
    template_name='CourseCreate.html'
    fields = '__all__'
    # context_object_name='courses'
    
    
