from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    bio = models.TextField(max_length=90,default="")
    def __str__(self):
        return self.first_name +" "+ self.email

class AddressDetails(models.Model):
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name+" "+ self.user.email + self.address


    