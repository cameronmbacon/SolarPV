from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=25)
    First_Name = models.CharField(max_length=50)
    Middle_Initial = models.CharField(max_length=5)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=255)
    Gender = models.CharField(max_length=10)
    Street_Address = models.CharField(max_length=255)
    City = models.CharField(max_length=50)
    US_State = models.CharField(max_length=4)
    Zipcode = models.IntegerField()
    Phone_Number = models.CharField(max_length=25)
    Company = models.CharField(max_length=50)
    class Meta:
        db_table = 'user_tbl'