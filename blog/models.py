from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    add_date=models.DateField(auto_created=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='data', null=True, blank=True)

    def __str__(self):
        return '{}/{}'.format  (self.title,self.add_date)

    def __unicode__(self):
        return 
