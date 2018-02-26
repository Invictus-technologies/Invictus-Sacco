from django.db import models
from .helpers import RandomFileName 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Member_reg(models.Model):
    fullname = models.CharField(max_length=100)
    dob = models.DateField(max_length=50)
    idno = models.IntegerField()
    member_no = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=20)
    employer = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    kin_fullname = models.CharField(max_length=100)
    kin_phone = models.IntegerField()
    kin_id = models.IntegerField()
    kin_relation = models.CharField(max_length=70)
    datestamp = models.DateField()
    transaction_reference = models.CharField(max_length=80)


    def __str__(self):
        return self.idno

class reg_members(models.Model):
    fullname = models.CharField(max_length=100)
    dob = models.DateField(max_length=50)
    idno = models.IntegerField()
    member_no = models.IntegerField()
    mobile = models.IntegerField()
    month_cont = models.IntegerField()
    email = models.EmailField(max_length=100)
    employer = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    kin_fullname = models.CharField(max_length=100)
    kin_phone = models.IntegerField()
    kin_id = models.IntegerField()
    kin_relation = models.CharField(max_length=70)
    datestamp = models.DateField()
    transaction_reference = models.CharField(max_length=80)


    def __str__(self):
        return self.idno



class Uploads(models.Model):
    idno = models.IntegerField()
    id_front = models.ImageField(upload_to=RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/ids/'))
    id_back = models.ImageField(upload_to=RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/ids/'))
    KRA = models.FileField(upload_to=RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/kra/'))
    passport = models.FileField(null=True ,upload_to=RandomFileName('/home/gathage/jungle/Sacco/invictus/static/invictus/uploads/passport/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    username = models.IntegerField()
    email = models.EmailField(max_length=100 ,  null=True)
    set_password = models.CharField(max_length=100)
    
