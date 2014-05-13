from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sprint(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField()

class Comment(models.Model):
    text = models.TextField()
    sprint = models.ForeignKey(Sprint, related_name='comment_sprint')
    

class Issue(models.Model):

    URGENCY = (
        ('1', 'Laag'),
        ('2', 'Medium'),
        ('3', 'Hoog'),
    )

    STATUS = (
        ('1', 'Ontwikkeld'),
        ('2', 'Getest'), 
     )

    sprint = models.ForeignKey(Sprint, related_name='issue_sprint')
    title = models.CharField(max_length=50)
    description = models.TextField()
    urgency = models.CharField(max_length=1, choices=URGENCY)
    submitter = models.ForeignKey(User, related_name='submitter')
    assignee = models.ForeignKey(User, related_name='assignee')
    estimated_time = models.IntegerField()
    spend_time = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS)




