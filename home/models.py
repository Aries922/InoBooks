from django.db import models
from django.contrib.auth.models import User
from  django.utils.timezone import now

# Create your models here.




class Booksp(models.Model):
    # print(User)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    author =models.CharField(max_length=150)
    Description =models.CharField(max_length=300,blank=True)
    pdf =models.FileField(null=True,blank=False)
    img = models.ImageField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return self.name

class bookreport(models.Model):
    sno= models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    books = models.ForeignKey(Booksp,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)


