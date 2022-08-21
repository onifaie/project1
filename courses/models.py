from cProfile import label
from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

# Create your models here.
class gatogery_course(models.Model):
    title_gatogery=models.CharField(max_length=100)
    add_date=models.DateField(auto_created=True)
    
    def __str__(self):
        return self.title_gatogery

    



class courses(models.Model):
    course_name=models.CharField(max_length=100)
    hours=models.IntegerField(default=0)
    course_lesson=models.IntegerField(default=0)
    image_course=models.ImageField(upload_to='image_course')
    summary_course=models.TextField(max_length=500)
    add_date=models.DateField(auto_created=True)
    course_price=models.IntegerField(default=0)
    user_course = models.ForeignKey(User, on_delete=models.CASCADE)
    gatogery=models.ForeignKey(gatogery_course, on_delete=models.CASCADE, related_name='course_gatogery',default=1)
    
    
    def __str__(self):
        return '{}/{}'.format  (self.course_name,self.summary_course)

    def __unicode__(self):
        return 



class lesson(models.Model):
    lesson_title=models.CharField(max_length=100)
    lesson_course=models.ForeignKey(courses,on_delete=models.CASCADE,name='course_lesson')
    lesson_longTime=models.IntegerField(default=0)
    lesson_content=models.TextField(max_length=500)
    lesson_homework=models.TextField(max_length=1000)
    lesson_video=models.FileField(upload_to='video_lesson')
    
      
    def __str__(self):
        return '{}'.format  (self.lesson_title)
    
    
class comment_lesson(models.Model):
        comment_date=models.DateField(auto_created=True)
        comment=models.TextField(max_length=500)
        comment_lesson=models.ForeignKey('lesson',on_delete=models.CASCADE,name='lesson_comment')
        comment_user=models.ForeignKey(User,on_delete=models.CASCADE,name='comment_user')
        comment_course=models.ForeignKey(courses,on_delete=models.CASCADE,name='comment_course')
        
        def __str__(self):
         return '{}'.format  (self.comment_date)
    
  
 
    
    
    