from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(default=0)
    fname = models.CharField(max_length=20,default="")
    lname = models.CharField(max_length=20,default="")
    pnum = models.CharField( max_length=10)
    email = models.EmailField(max_length=50, default="")

    class Meta:
        db_table = "employee"
    def __str__(self):
        return self.fname
