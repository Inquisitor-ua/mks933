from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class News(models.Model):
    header = models.CharField(max_length=200, verbose_name='Header of new')
    text = models.TextField(verbose_name='Text of new')
    created_at = models.DateTimeField(verbose_name='Creating time of new', auto_now=True, auto_created=True)
    image = models.ImageField(verbose_name='Image', upload_to='news/', blank= True, null= True)
    def __str__(self):
        return f"{self.header}-{self.created_at}"
        
class Schoolclasses(models.Model):
    class_name = models.CharField(max_length=200, verbose_name='Name of class')
    class_level = models.IntegerField(verbose_name='Level of class')
    def __str__(self):
        return f"{self.class_name}-{self.class_level}"

class Customuser(AbstractUser):
    biography = models.TextField(verbose_name='Bio of user', null= True, blank= True)
    phone_number = models.CharField(max_length=50, verbose_name='Phone Number of user', null= True, blank= True)
    birthday_date = models.DateField(verbose_name='Birthday date of user', null= True, blank= True)
    def __str__(self):
        return f"{self.username}"


