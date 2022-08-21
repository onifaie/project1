from cProfile import label
from django.db import models

# Create from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

class Kindjop(models.Model):
    name_jop=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name_jop

    

class CityJop(models.Model):
    City_jop=models.CharField(max_length=100)
    
    def __str__(self):
        return self.City_jop

   
class Cetivcation(models.Model):
    level_Cetivcation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.level_Cetivcation

    
    
class LookingJop(models.Model):
    name=models.CharField( max_length=100,verbose_name='اسم الموظف ')
    brith_date=models.DateField(verbose_name='تاريخ الميلاد')
    Kindjop=models.ForeignKey(Kindjop,on_delete=models.CASCADE,related_name='jop_kind',verbose_name='اسم الوظيفة')
    City_jop=models.ForeignKey(CityJop,on_delete=models.CASCADE,related_name='Jop_City',verbose_name='مدينه الوظيفة')
    Cetivcation=models.ForeignKey(Cetivcation,on_delete=models.CASCADE,related_name='Jop_Cetivcation',verbose_name='الموهل ')
    experince=models.IntegerField(verbose_name='سنوات الخبرة ')
    mobile_No=models.CharField(max_length=13,verbose_name='رقم الجوال ')
    Email=models.EmailField(max_length=100,verbose_name='البريد الالكتروني')
    files=models.FileField(upload_to='jopfile')
    # memo=models.TextField(max_length=800,nullable=True)
    
    def __str__(self):
        return self.name
