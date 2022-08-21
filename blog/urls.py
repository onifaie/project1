
from argparse import Namespace
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('blog/', views.all_blog, name='all_post'),
    path('add_new/', views.add_new,name='add_new'), 
    path('blog/edit_blog/<int:id>', views.edit_blog, name='edit_blog'), 
   




 
    # path('', views.index, name='index'),   
 ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)