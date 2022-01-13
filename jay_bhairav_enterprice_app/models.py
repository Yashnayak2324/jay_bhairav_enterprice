from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Phone_No = models.CharField(max_length=12)
    Message = models.CharField(max_length=800)

    def __str__(self):
        return self.Name 

class Category(models.Model):
    Category_Name = models.CharField(max_length=100)
    Title = models.CharField(max_length=100,default="",null=True)
    Img = models.ImageField(upload_to='Images/',default="",null=True)

    def __str__(self):
        return self.Category_Name

class Product_Details(models.Model):    
    Name = models.ForeignKey(Category,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100,default="",null=True)
    img1 = models.ImageField(upload_to='Images/',default="",null=True)

    def __str__(self):
        return self.Title + " " + self.Name.Category_Name

class Subscribe(models.Model):
    Email = models.EmailField()

    def __str__(self):
        return self.Email

class Catlog(models.Model):
    Name = models.CharField(max_length=100)
    File = models.FileField(upload_to='files/',default="Abc.pdf")

    def __str__(self):
        return self.Name

