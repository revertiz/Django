from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #one to many relationship (user to many posts)

# Create your models here.
class Post(models.Model): #database klase
    title = models.CharField(max_length=100) #atributai
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now_add=True bet negalima bus keisti on edit laiko
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #magic/special method __str__
        return self.title

# python manage.py sqlmigrate name - parodo SQL koda
# makemigrations ir po to migrate
