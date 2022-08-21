from django.shortcuts import render,redirect
from .models import blog
from .forms import myforms


def all_blog(request):
        
    post=blog.objects.all()
    form=myforms()
    return render(request, 'indexblog.html',{'post':post,'form':form})

# Create your views here.


# def add_newblog(request):
#     form = myforms(request.POST)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         # post.add_date = timezone.now()
#         post.save()
        
        
def index(request):
    return render(request,'index.html')

def test (request):
    return render(request,'test.html')



def add_new(request):
    if request.method == "POST":
        form = myforms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('all_post')
    else:
        form = myforms()
    return render(request, 'add_new.html', {'form': form})




# def edit_blog(request,id):
#     myblog=blog.objects.get(id=id)
#     # form = myforms(request.post, instance=myblog)



#     if request.method == "POST":
#         form = myforms(request.POST,instance=myblog)


#         if form.is_valid():
#             # blog = form.save(commit=False)
#             # blog.author = request.user
#             blog.save()
#             return redirect('all_post')
#     else:
#             form = myforms(instance=form)
#             context={
#                 'form':form
#                     }
       
#     return render(request, 'edit.html', context)



def edit_blog(request, id):
    band = blog.objects.get(id=id)

    if request.method == 'POST':
        form = myforms(request.POST,request.FILES,instance=band )
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('all_post')
    else:
        form = myforms(instance=band)

    return render(request,
                'edit.html',
                {'form': form})