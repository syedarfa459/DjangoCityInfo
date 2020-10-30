from django.db import models

# Create your models here.
class Contact(models.Model):
    UserName=models.CharField(max_length=50)
    PhoneNumber=models.CharField(max_length=12)
    City=models.CharField(max_length=20)
    Useradvice=models.CharField(max_length=300)

    def __str__(self):
        return self.UserName
    