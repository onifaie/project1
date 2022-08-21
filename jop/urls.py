
from argparse import Namespace
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
# from .views import view
from .views import LookingJopCreate ,LookingJopDetails,LookingJopDelete

urlpatterns = [
   
    
    path('', views.xx,name='mainjop'),
    path('create',LookingJopCreate.as_view() ,name='LookingCreate'), 
    path('/edit/<int:pk>',LookingJopDetails.as_view() ,name='LookingJopDetails'), 
    path('/delete/<int:pk>',LookingJopDelete.as_view() ,name='LookingJopDelete'), 

    # path('blog/edit_blog/<int:id>', views.edit_blog, name='edit_blog'), 
   




 
    # path('', views.index, name='index'),   
 ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)