from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# field designing 
class Chaivariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
    ]
    name=models.CharField( max_length=50)
    image= models.ImageField(upload_to='firstapps/')
    date=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self) -> str:
        return self.name
    

    #one to many

class chaireview(models.Model):
    chai=models.ForeignKey(Chaivariety,on_delete=models.CASCADE,related_name="reviews")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    #to look better as object in database

    def __str__(self) -> str:
        return f'{self.user.username} review for {self.chai.name}'  


    #many to many

class stores(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_variety=models.ManyToManyField(Chaivariety,related_name="stores")


    def __str__(self) -> str:
        return self.name


    #one to one

class certificate(models.Model):
    chai=models.OneToOneField(Chaivariety,on_delete=models.CASCADE,related_name="certify") 
    certify_number=models.CharField( max_length=50)   
    issued_date=models.DateTimeField(default=timezone.now)
    validity=models.DateTimeField() 


    def __str__(self) -> str:
        return f'certificate for  {self.chai}' 