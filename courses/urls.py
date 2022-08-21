
from argparse import Namespace
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CourseList,CouresDetail,CouresCreate

urlpatterns = [
    path('zz',views.CourseList.as_view(),name='list'),
    path('zy/<int:pk>',views.CouresDetail.as_view(),name='Details'),
    
    path('new',views.CouresCreate.as_view(),name='CourseCreate'),



    path('',views.all_courses, name='all_courses'),
    path('add_new_course', views.add_new_course, name='add_new_course'),

    
    # path('add_new/', views.add_new,name='add_new'), 
    # path('blog/edit_blog/<int:id>', views.edit_blog, name='edit_blog'), 
   




 
    # path('', views.index, name='index'),   
 ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)