from django.db import models

# Create your models here.
class Subscribe(models.Model):
    email = models.CharField(max_length=155)
    date = models.DateField()
    def __str__(self):
        return self.email
    
class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    phone = models.CharField(max_length=155)
    password = models.CharField(max_length=155)
    subject = models.CharField(max_length=155)
    textarea = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class SignUp(models.Model):
    username = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=155)
    repeatpassword = models.CharField(max_length=155)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
