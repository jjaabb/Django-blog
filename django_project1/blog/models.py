from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): #we have a title that will be a field of our post
    title = models.CharField(max_length=100)#table of our data base
    #character field that has a restriction of max length 100
    content = models.TextField()#post content table
    date_posted = models.DateTimeField(default=timezone.now)
    #date when post was posted table (imported module for that timezone)
    #don't need now() because we want  to pass in the actual function
    # as defautl value, not execute function!!!
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #is user is deleted than all his posts will be deleted too.

    def __str__(self):
        return self.title