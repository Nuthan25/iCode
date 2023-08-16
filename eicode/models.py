from django.db import models

# Create your models here.
class contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True)
    phoneno=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20,null=True)
    msg=models.CharField(max_length=20,null=True)

class registration(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True)
    phoneno=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20,null=True)
    
    c_programming = models.BooleanField(default=False)
    java = models.BooleanField(default=False)
    html_css = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    react_js = models.BooleanField(default=False)
    sql = models.BooleanField(default=False)
    cpp = models.BooleanField(default=False)
    mongodb = models.BooleanField(default=False)
    program_period = models.CharField(max_length=20,null=True)
    
    card_number = models.CharField(max_length=16,null=True)
    cvv = models.CharField(max_length=3,null=True)