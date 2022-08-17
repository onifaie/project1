from django.shortcuts import render

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