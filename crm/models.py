from django.db import models

# Create your models here.

class Empolyees(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    contact=models.CharField(null=True,max_length=200,blank=True)
    age=models.PositiveBigIntegerField()
    profile_pic=models.ImageField(upload_to="image",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)


    def __str__(self):
        return self.name
    
